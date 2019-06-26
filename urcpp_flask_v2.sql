-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2019 at 07:28 PM
-- Server version: 5.5.57-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `urcpp_flask_v2`
--

-- --------------------------------------------------------

--
-- Table structure for table `budget`
--

CREATE TABLE IF NOT EXISTS `budget` (
  `bID` int(11) NOT NULL AUTO_INCREMENT,
  `facultyStipend` int(11) DEFAULT NULL,
  `facultyStipendDesc` text NOT NULL,
  `miles` int(11) DEFAULT NULL,
  `milesDesc` text NOT NULL,
  `otherTravel` int(11) DEFAULT NULL,
  `otherTravelDesc` text NOT NULL,
  `equipment` int(11) DEFAULT NULL,
  `equipmentDesc` text NOT NULL,
  `materials` int(11) DEFAULT NULL,
  `materialsDesc` text NOT NULL,
  `other` int(11) DEFAULT NULL,
  `otherDesc` text NOT NULL,
  PRIMARY KEY (`bID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=42 ;

--
-- Dumping data for table `budget`
--

INSERT INTO `budget` (`bID`, `facultyStipend`, `facultyStipendDesc`, `miles`, `milesDesc`, `otherTravel`, `otherTravelDesc`, `equipment`, `equipmentDesc`, `materials`, `materialsDesc`, `other`, `otherDesc`) VALUES
(1, NULL, '', NULL, '', NULL, '', NULL, '', NULL, '', NULL, ''),
(2, NULL, '', NULL, '', NULL, '', NULL, '', NULL, '', NULL, ''),
(3, 800, '', 0, '', 0, '', 800, '', 800, '', 8300, ''),
(4, NULL, '', NULL, '', NULL, '', NULL, '', NULL, '', NULL, ''),
(5, 56767, '', 68786, '', 6876, '', 6768786, '', 68767, '', 78678, ''),
(6, 2147483647, '', 46786786, '', 541646, '', 2147483647, '', 56464634, '', 6786781, ''),
(7, 2, '', 2, '', 2, '', 2, '', 2, '', 2, ''),
(8, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(9, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(10, 1, '1', 1, '1', 1, '1', 1, '1', 1, '1', 1, '1'),
(11, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(12, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(13, 128, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(14, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(15, 1, '', 50, '', 4, '', 2, '', 3, '', 5, ''),
(16, 2, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(17, 5301, '', 5, '', 1, '', 1, '', 1, '', 1, ''),
(18, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(19, 9333, '', 3, '', 3, '', 33, '', 3, '', 3, ''),
(20, 888888, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(21, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(22, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(23, 5300, '', 1, '', 1, '', 1, '', 1, '', 0, ''),
(24, 800, '', 8, '', 800, '', 800, '', 800, '', 0, ''),
(25, 10, '', 10, '', 10, '', 10, '', 10, '', 10, ''),
(26, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(27, 11, '', 1, '', 1, '', 1, '', 1, '', 2147483647, ''),
(28, 1, '', 1, '', 3, '', 1, '', 1, '', 2, ''),
(29, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(30, 1, '', 1, '', 1, '', 1, '', 1, '', 0, ''),
(31, 2, '', 2, '', 2, '', 2, '', 2, '', 2, ''),
(32, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(33, 1, '', 1, '', 1, '', 1, '', 0, '', 1, ''),
(34, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(35, 830000, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(36, 1, '', 1, '', 1, '', 1, '', 1, '', 83000, ''),
(37, 12222, '', 12, '', 12, '', 122, '', 7, '', 12, ''),
(38, 999, '', 1, '', 1, '', 9, '', 1, '', 1, ''),
(39, 1, '', 1, '', 1, '', 1, '', 1, '', 99, ''),
(40, 1, '', 1, '', 1, '', 1, '', 1, '', 1, ''),
(41, 60, '', 1, '', 1, '', 1, '', 1, '', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `collaborators`
--

CREATE TABLE IF NOT EXISTS `collaborators` (
  `cID` int(11) NOT NULL AUTO_INCREMENT,
  `pID_id` int(11) NOT NULL,
  `username_id` varchar(255) NOT NULL,
  `yearsFunded` text NOT NULL,
  PRIMARY KEY (`cID`),
  KEY `collaborators_pID_id` (`pID_id`),
  KEY `collaborators_username_id` (`username_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `emailtemplates`
--

CREATE TABLE IF NOT EXISTS `emailtemplates` (
  `eID` int(11) NOT NULL AUTO_INCREMENT,
  `Body` text,
  `Subject` text,
  PRIMARY KEY (`eID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `emailtemplates`
--

INSERT INTO `emailtemplates` (`eID`, `Body`, `Subject`) VALUES
(1, '<p>Date: January 25, 2016 To: Maggie Robillard From: Undergraduate Research and Creative Projects Program Committee Chair: Martin Veillette Members: Ian Norris, Wayne Messer, Kennaria Brown, Eric Pearson, Althea Webb</p><p>@@Start Date@@@@Start Date@@@@ProjectTitle@@@@Students@@@@Year@@@@Date@@@@Faculty@@@@Date@@@@End Date@@@@Stipend@@</p><p>Re: Summer 2017 Undergraduate Research and Creative Projects Program proposal The Undergraduate Research and Creative Projects Program (URCPP) Committee is pleased to approve your request for funding for your summer 2017 faculty-student research project. The URCPP will fund $8300.00 on your project: Analyzing Trade Books and Other Print Media for Classroom Use, contingent on IRB approval if your research involves human subjects. Your program will run from May 29- July 26, 2017. Your stipend of $5,300 will be disbursed in one payment in June. You will be notified by Jim Strand which account number to use to report expenses for your project. He also will provide instructions to follow for obtaining reimbursements. Be sure to stay within the approved budget amount mentioned above. If you receive additional funding for this project not already indicated in your proposal, please alert Sarah Broomfield, because that may affect your eligibility for this URCPP award. Your project has been approved for working with 3 students -- yet to be determined. When you have selected your student researchers, send Sarah Broomfield their name(s) and B-numbers (send to broomfields@berea.edu) and she will create an electronic labor status form which will be copied to the student, to you as the supervisor, and to the Student Labor Office. The student information will also be shared with the Student Service Center to enroll them in UGR 010 which, upon satisfactory completion, will earn an ALE credit, but does not earn credit towards graduation. Please be aware that students cannot be enrolled in another summer course at the same time as they are enrolled in UGR 010 (including the first four-week or eight-week summer sessions, internships, independent studies, other non-credit courses, etc.) and participate in summer research funded by the URCPP. There are some requirements you must fulfill as a faculty member receiving URCPP funding. Failure to complete the following requirements will affect future URCPP funding. 1. You are required to submit an &ldquo;S&rdquo; or &ldquo;U&rdquo; grade to Associate Registrar Kathy Wallace for each student&rsquo;s participation in the research/creative project. Your grades must be submitted before Thanksgiving Break. 2. You are required to administer a Pre-Research Survey and Post-Research Survey to each student working with your project. Details about the surveys will be forthcoming. You and your students must participate in the weekly summer discussions where student researchers will be asked to share the progress they are making on their research. 3. You are required to electronically submit an abstract and a one-page summary of the project, which is due to the Academic Vice President&rsquo;s Office no later than August 21, 2017. The abstract will be shared with the Development office (for donors) and published in the annual Journal of Undergraduate Research Abstracts, compiled by Ron Rosen; thus, it can be discipline-specific. The report is shared with the Academic Vice President and Dean of the Faculty and should be geared toward a more general audience. 4. You are also required to participate in the Berea Undergraduate Research Symposium (BURS) in early October 2017. 5. If your research involves human subjects, your funding is subject to IRB approval and you must complete and submit an application to the IRB by March 13, 2017. Please see the following definition in the faculty manual to confirm whether you research does or does need IRB approval http://catalog.berea.edu/en/Current/Catalog/Selected-Institution-Wide-Policies/Research-Involving-Human-Subjects). No URCPP funds will be dispersed to any research involving human subjects who has not received IRB approval. Questions regarding IRB application can be directed to the IRB chair, Wendy Williams (williams@berea.edu). If you have any questions, please feel free to contact any member of the URCPP Committee. Congratulations and best wishes on the project! Sincerely, Martin Veillette URCPC Chair cc: Linda Strong-Leek</p><p>&nbsp;</p>', 'Research ');

-- --------------------------------------------------------

--
-- Table structure for table `ldapfaculty`
--

CREATE TABLE IF NOT EXISTS `ldapfaculty` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `bnumber` text NOT NULL,
  `lastname` text NOT NULL,
  `firstname` text NOT NULL,
  `isChair` tinyint(1) NOT NULL,
  `isCommitteeMember` tinyint(1) NOT NULL,
  PRIMARY KEY (`fID`),
  UNIQUE KEY `ldapfaculty_username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `ldapfaculty`
--

INSERT INTO `ldapfaculty` (`fID`, `username`, `bnumber`, `lastname`, `firstname`, `isChair`, `isCommitteeMember`) VALUES
(1, 'jadudm', 'B00669796', 'Jadud', 'Matt', 1, 1),
(2, 'heggens', 'B00660000', 'Heggen', 'Scott', 1, 1),
(3, 'nakazawam', 'B00661111', 'Nakazawa', 'Mario', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `ldapstudents`
--

CREATE TABLE IF NOT EXISTS `ldapstudents` (
  `username` int(11) NOT NULL AUTO_INCREMENT,
  `bnumber` text NOT NULL,
  `lastname` text NOT NULL,
  `firstname` text NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `parameters`
--

CREATE TABLE IF NOT EXISTS `parameters` (
  `pID` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `appOpenDate` datetime NOT NULL,
  `appCloseDate` datetime NOT NULL,
  `mileageRate` float NOT NULL,
  `laborRate` float NOT NULL,
  `isCurrentParameter` tinyint(1) NOT NULL,
  PRIMARY KEY (`pID`),
  UNIQUE KEY `parameters_year` (`year`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `parameters`
--

INSERT INTO `parameters` (`pID`, `year`, `appOpenDate`, `appCloseDate`, `mileageRate`, `laborRate`, `isCurrentParameter`) VALUES
(1, 2016, '2015-12-01 00:00:00', '2016-01-01 11:55:00', 111, 1, 1),
(3, 2015, '2019-05-01 00:00:00', '2019-11-28 11:55:00', 0.49, 0.42, 0),
(7, 2017, '2019-05-02 00:00:00', '2019-05-02 11:55:00', 0.1, 0.1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `postsurvey`
--

CREATE TABLE IF NOT EXISTS `postsurvey` (
  `psID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`psID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `presurvey`
--

CREATE TABLE IF NOT EXISTS `presurvey` (
  `psID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`psID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `programs`
--

CREATE TABLE IF NOT EXISTS `programs` (
  `pID` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `abbreviation` text NOT NULL,
  PRIMARY KEY (`pID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `programs`
--

INSERT INTO `programs` (`pID`, `name`, `abbreviation`) VALUES
(1, 'Computer and Information Science', 'CSC'),
(2, 'Biology', 'BIO'),
(3, 'Physics', 'PHY');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE IF NOT EXISTS `projects` (
  `pID` int(11) NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `budgetID_id` int(11) NOT NULL,
  `duration` int(11) NOT NULL,
  `startDate` datetime NOT NULL,
  `endDate` datetime NOT NULL,
  `year_id` int(11) NOT NULL,
  `hasCommunityPartner` tinyint(1) NOT NULL,
  `isServiceToCommunity` tinyint(1) NOT NULL,
  `humanSubjects` tinyint(1) DEFAULT NULL,
  `numberStudents` int(11) NOT NULL,
  `status` text NOT NULL,
  `createdDate` datetime NOT NULL,
  PRIMARY KEY (`pID`),
  KEY `projects_budgetID_id` (`budgetID_id`),
  KEY `projects_year_id` (`year_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=41 ;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`pID`, `title`, `budgetID_id`, `duration`, `startDate`, `endDate`, `year_id`, `hasCommunityPartner`, `isServiceToCommunity`, `humanSubjects`, `numberStudents`, `status`, `createdDate`) VALUES
(1, 'Test', 1, 9, '2019-05-01 00:00:00', '2019-07-03 00:00:00', 2016, 0, 0, 0, 4, 'Withdrawn', '2019-05-09 18:47:08'),
(2, 'test1', 3, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 1, 0, 1, 'Withdrawn', '2019-05-10 12:50:10'),
(3, 'test1', 4, 10, '2019-05-09 00:00:00', '2019-07-18 00:00:00', 2016, 0, 1, 0, 1, 'Withdrawn', '2019-05-10 17:47:37'),
(4, 'ewfrg', 5, 0, '2019-05-02 00:00:00', '2019-05-02 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-10 18:20:33'),
(5, 'ewvgf', 6, 9, '2019-05-09 00:00:00', '2019-07-11 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-10 18:22:21'),
(6, 'test1', 7, 10, '2019-05-03 00:00:00', '2019-07-12 00:00:00', 2016, 0, 1, 0, 1, 'Withdrawn', '2019-05-10 18:51:18'),
(7, 'Added $ to milage and labor rate', 8, 9, '2019-05-01 00:00:00', '2019-07-03 00:00:00', 2016, 0, 0, 0, 1, 'Pending', '2019-05-10 20:32:21'),
(8, 'test1', 9, 8, '2019-05-02 00:00:00', '2019-06-27 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-13 13:06:27'),
(9, 'test1', 10, 9, '2019-05-03 00:00:00', '2019-07-05 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-13 15:48:49'),
(10, 'Added $ to milage and labor rate', 11, 9, '2019-05-02 00:00:00', '2019-07-04 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-13 19:06:28'),
(11, 'test1', 12, 0, '2019-05-01 00:00:00', '2019-05-01 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-13 19:11:38'),
(12, 'test1', 13, 8, '2019-05-02 00:00:00', '2019-05-02 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-13 19:57:13'),
(13, 'test1', 14, 10, '2019-05-03 00:00:00', '2019-07-12 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-13 20:08:20'),
(14, 'test1', 15, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-15 13:59:58'),
(15, 'Added $ to milage and labor rate', 16, 0, '2019-05-02 00:00:00', '2019-05-02 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-05-15 15:13:50'),
(16, 'test1', 17, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-15 15:20:43'),
(17, 'ewfrg', 18, 9, '2019-05-02 00:00:00', '2019-07-04 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-15 17:49:41'),
(18, 'test1', 19, 10, '2019-05-01 00:00:00', '2019-07-10 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-05-15 17:59:18'),
(19, 'test1', 20, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-15 19:24:45'),
(20, 'test1', 21, 9, '2019-05-01 00:00:00', '2019-07-03 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-15 19:26:38'),
(21, 'test1', 22, 9, '2019-05-01 00:00:00', '2019-07-03 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-15 19:41:00'),
(22, 'Fridaaaaaaaaaaay', 23, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-17 14:01:25'),
(23, 'File downloads now working', 24, 9, '2019-05-01 00:00:00', '2019-07-03 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-20 17:42:48'),
(24, 'fgd', 25, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-21 18:35:22'),
(25, 'ghfmhjg', 26, 9, '2019-05-01 00:00:00', '2019-07-03 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-21 19:27:13'),
(26, 'Ayyy', 27, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-23 13:41:23'),
(27, 'Added $ to milage and labor rate', 28, 8, '2019-05-03 00:00:00', '2019-06-28 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-23 20:27:17'),
(28, 'Friday testin', 29, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-24 14:50:24'),
(29, 'Ayyy', 30, 0, '2019-05-01 00:00:00', '2019-05-01 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-24 14:53:31'),
(30, 'Ayyy', 31, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-05-24 14:56:17'),
(31, 'Thursday''s test', 32, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-30 14:45:46'),
(32, '9ayyyyyrtsrdtgs', 33, 10, '2019-05-01 00:00:00', '2019-07-10 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-05-30 14:47:46'),
(33, 'Thursday''s test', 34, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-05-30 15:01:27'),
(34, 'Fridaaaaaaaaaaaaaaaaaaaay', 35, 8, '2019-05-01 00:00:00', '2019-06-26 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-05-31 12:54:51'),
(35, 'Fridaaaaaaaaaaaaaaaaaaaay', 36, 8, '2019-06-01 00:00:00', '2019-07-27 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-06-03 13:22:24'),
(36, 'mondaze', 37, 9, '2019-06-01 00:00:00', '2019-08-03 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-06-03 14:38:05'),
(37, 'modal on /budget is STILL FiRING?!', 38, 8, '2019-06-01 00:00:00', '2019-07-27 00:00:00', 2016, 0, 0, 0, 1, 'Withdrawn', '2019-06-03 17:59:44'),
(38, 'modal on /budget is STILL FiRING?!', 39, 8, '2019-06-06 00:00:00', '2019-08-01 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-06-03 19:38:48'),
(39, 'when yankees start talkin shit', 40, 8, '2019-06-01 00:00:00', '2019-07-27 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-06-04 17:59:01'),
(40, 'avocardo did 9/11', 41, 8, '2019-06-01 00:00:00', '2019-07-27 00:00:00', 2016, 0, 0, NULL, 1, 'Withdrawn', '2019-06-04 18:03:12');

-- --------------------------------------------------------

--
-- Table structure for table `urcppfaculty`
--

CREATE TABLE IF NOT EXISTS `urcppfaculty` (
  `fID` int(11) NOT NULL AUTO_INCREMENT,
  `pid_id` int(11) NOT NULL,
  `username_id` varchar(255) NOT NULL,
  `yearsFunded` text NOT NULL,
  `relatedFunding` text NOT NULL,
  `programID_id` int(11) NOT NULL,
  PRIMARY KEY (`fID`),
  KEY `urcppfaculty_pid_id` (`pid_id`),
  KEY `urcppfaculty_username_id` (`username_id`),
  KEY `urcppfaculty_programID_id` (`programID_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `urcppfaculty`
--

INSERT INTO `urcppfaculty` (`fID`, `pid_id`, `username_id`, `yearsFunded`, `relatedFunding`, `programID_id`) VALUES
(1, 40, 'jadudm', '{\nelevenPlus: true, \n}', '', 2),
(2, 7, 'heggens', '{\nsixToTenyr: true, \n}', '', 2);

-- --------------------------------------------------------

--
-- Table structure for table `urcppstudents`
--

CREATE TABLE IF NOT EXISTS `urcppstudents` (
  `sID` int(11) NOT NULL AUTO_INCREMENT,
  `username_id` int(11) NOT NULL,
  `preSurveyID_id` int(11) NOT NULL,
  `postSurveyID_id` int(11) NOT NULL,
  `projectID_id` int(11) NOT NULL,
  PRIMARY KEY (`sID`),
  KEY `urcppstudents_username_id` (`username_id`),
  KEY `urcppstudents_preSurveyID_id` (`preSurveyID_id`),
  KEY `urcppstudents_postSurveyID_id` (`postSurveyID_id`),
  KEY `urcppstudents_projectID_id` (`projectID_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `voting`
--

CREATE TABLE IF NOT EXISTS `voting` (
  `vID` int(11) NOT NULL AUTO_INCREMENT,
  `committeeID_id` varchar(255) NOT NULL,
  `projectID_id` int(11) NOT NULL,
  `studentLearning` float DEFAULT NULL,
  `studentAccessibility` float DEFAULT NULL,
  `qualityOfResearch` float DEFAULT NULL,
  `studentDevelopment` float DEFAULT NULL,
  `facultyDevelopment` float DEFAULT NULL,
  `collaborative` float DEFAULT NULL,
  `interaction` float DEFAULT NULL,
  `communication` float DEFAULT NULL,
  `scholarlySignificance` float DEFAULT NULL,
  `proposalQuality` float DEFAULT NULL,
  `budget` float DEFAULT NULL,
  `timeline` float DEFAULT NULL,
  `comments` text,
  PRIMARY KEY (`vID`),
  KEY `voting_committeeID_id` (`committeeID_id`),
  KEY `voting_projectID_id` (`projectID_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `voting`
--

INSERT INTO `voting` (`vID`, `committeeID_id`, `projectID_id`, `studentLearning`, `studentAccessibility`, `qualityOfResearch`, `studentDevelopment`, `facultyDevelopment`, `collaborative`, `interaction`, `communication`, `scholarlySignificance`, `proposalQuality`, `budget`, `timeline`, `comments`) VALUES
(1, 'jadudm', 22, 5, 4, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, '');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `collaborators`
--
ALTER TABLE `collaborators`
  ADD CONSTRAINT `collaborators_ibfk_1` FOREIGN KEY (`pID_id`) REFERENCES `projects` (`pID`),
  ADD CONSTRAINT `collaborators_ibfk_2` FOREIGN KEY (`username_id`) REFERENCES `ldapfaculty` (`username`);

--
-- Constraints for table `projects`
--
ALTER TABLE `projects`
  ADD CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`budgetID_id`) REFERENCES `budget` (`bID`),
  ADD CONSTRAINT `projects_ibfk_2` FOREIGN KEY (`year_id`) REFERENCES `parameters` (`year`);

--
-- Constraints for table `urcppfaculty`
--
ALTER TABLE `urcppfaculty`
  ADD CONSTRAINT `urcppfaculty_ibfk_1` FOREIGN KEY (`pid_id`) REFERENCES `projects` (`pID`),
  ADD CONSTRAINT `urcppfaculty_ibfk_2` FOREIGN KEY (`username_id`) REFERENCES `ldapfaculty` (`username`),
  ADD CONSTRAINT `urcppfaculty_ibfk_3` FOREIGN KEY (`programID_id`) REFERENCES `programs` (`pID`);

--
-- Constraints for table `urcppstudents`
--
ALTER TABLE `urcppstudents`
  ADD CONSTRAINT `urcppstudents_ibfk_1` FOREIGN KEY (`username_id`) REFERENCES `ldapstudents` (`username`),
  ADD CONSTRAINT `urcppstudents_ibfk_2` FOREIGN KEY (`preSurveyID_id`) REFERENCES `presurvey` (`psID`),
  ADD CONSTRAINT `urcppstudents_ibfk_3` FOREIGN KEY (`postSurveyID_id`) REFERENCES `postsurvey` (`psID`),
  ADD CONSTRAINT `urcppstudents_ibfk_4` FOREIGN KEY (`projectID_id`) REFERENCES `projects` (`pID`);

--
-- Constraints for table `voting`
--
ALTER TABLE `voting`
  ADD CONSTRAINT `voting_ibfk_1` FOREIGN KEY (`committeeID_id`) REFERENCES `ldapfaculty` (`username`),
  ADD CONSTRAINT `voting_ibfk_2` FOREIGN KEY (`projectID_id`) REFERENCES `projects` (`pID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
