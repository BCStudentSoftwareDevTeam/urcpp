#lang racket
(require net/url
         net/url-connect)


(define port (make-parameter 80))
(define host (make-parameter "localhost"))

(define success 0)
(define failure 0)
(define ss (make-semaphore 1))
(define fs (make-semaphore 1))

(define (ping n)   
  (define ping-string (format "http://~a:~a/ping" (host) (port)))
  
  ;; (printf "Pinging [~a]~n" ping-string)
  (flush-output (current-output-port))
  (define ping-url (string->url ping-string))
  
  (define res (make-parameter false))
  (with-handlers ([exn? (λ (e) 
                          (semaphore-wait fs)
                          (set! failure (add1 failure))
                          (semaphore-post fs)
                          )])
    (define ip (get-pure-port ping-url))
    (res (port->string ip))
    (close-input-port ip))
  
  ;;(printf "RES: ~a~n" (res))
  (when (string? (res))
    ;;(printf "S: ~a~n" success)
    (semaphore-wait ss)
    (set! success (add1 success))
    ;;(printf "S: ~a~n" success)
    (semaphore-post ss)
    )
    ;; (printf "ping ~a: ~a~n" n data)
  )

(define (stress n)   
  (define stress-string (format "http://~a:~a/stress" (host) (port)))
  
  ;; (printf "Pinging [~a]~n" ping-string)
  (flush-output (current-output-port))
  (define stress-url (string->url stress-string))
  
  (define res (make-parameter false))
  (with-handlers ([exn? (λ (e) 
                          (semaphore-wait fs)
                          (set! failure (add1 failure))
                          (semaphore-post fs)
                          )])
    (define ip (get-pure-port stress-url))
    (res (port->string ip))
    (close-input-port ip))
  
  ;;(printf "RES: ~a~n" (res))
  (when (string? (res))
    ;;(printf "S: ~a~n" success)
    (semaphore-wait ss)
    (set! success (add1 success))
    ;;(printf "S: ~a~n" success)
    (semaphore-post ss)
    )
    ;; (printf "stress ~a: ~a~n" n (res))
  )

(define threads (make-parameter 3))
(define function (make-parameter ping))
(define seq (make-parameter false))

(command-line
 #:program "flask-stressor"
 #:once-each 
 [("-p" "--port") p
                  "Server port"
                  (port p)]
 [("-t" "--threads") t
                     "Number of threads to use"
                     (threads (string->number t))]
 
 [("--ping") "Ping the server"
             (function ping)]
 
 [("--stress") "Stress the server"
               (function stress)]
 
 [("--sequential") "Test each call sequentially"
                   (seq true)]
 
 [("--parallel") "Test the calls in parallel"
                   (seq false)]
 
 
 #:args ()
 
 ;; This is the parallel test
 (when (not (seq))
   (define tids
     (for/list ([i (range 0 (threads))])
       (thread (λ ()
                 ((function) i)))))
    (for-each thread-wait tids))

 
 ;; This is the sequential test
 (when (seq)
   (for/list ([i (range 0 (threads))])
     ((function) i)))
 
 (printf "~a threads, ~a success / ~a failures => ~a success~n"
         (threads) success failure 
         (exact->inexact
          (/ (floor (* 10 (/ success (+ success failure)))) 10))
 ))
 