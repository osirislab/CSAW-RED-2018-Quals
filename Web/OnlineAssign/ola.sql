-- phpMyAdmin SQL Dump
-- version 4.2.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Sep 24, 2018 at 12:43 AM
-- Server version: 5.5.38
-- PHP Version: 5.5.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `ola`
--

-- --------------------------------------------------------

--
-- Table structure for table `answer`
--

CREATE TABLE `answer` (
`id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `assignment`
--

CREATE TABLE `assignment` (
`id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `open_date` datetime NOT NULL,
  `due_date` datetime NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `assignment`
--

INSERT INTO `assignment` (`id`, `course_id`, `open_date`, `due_date`, `name`) VALUES
(1, 1, '2018-09-20 00:00:00', '2018-09-24 00:00:00', 'Assignment 1');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
`id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `instructor_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`id`, `name`, `instructor_id`) VALUES
(1, 'A course', 2);

-- --------------------------------------------------------

--
-- Table structure for table `enrollment`
--

CREATE TABLE `enrollment` (
  `course_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `enrollment`
--

INSERT INTO `enrollment` (`course_id`, `user_id`) VALUES
(1, 11);

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
`id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `instructor_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `assignment_id` int(11) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`id`, `student_id`, `instructor_id`, `question_id`, `assignment_id`, `message`) VALUES
(1, 11, 2, 2, 1, '<script>alert()</script>');

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
`id` int(11) NOT NULL,
  `assignment_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `body` text NOT NULL,
  `checker` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`id`, `assignment_id`, `name`, `body`, `checker`) VALUES
(1, 1, 'Textbook Question 5.12', 'What Is the airspeed velocity of an unladen swallow?', 'return strtolower($answer) == "african or european?";'),
(2, 1, 'Textbook Question 5.13', 'If a tree falls in a forest and no one is around to hear it, does it make a sound?', 'return strtolower($answer) == "yes";');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
`id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` binary(32) NOT NULL,
  `realname` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `realname`) VALUES
(1, 'superadmin', 0x7ad61b1db1fef10352abaa67634dfb072f98cbb581b4632c46cacfdca70a06d8, 'Super Admin'), -- ruPmE5tCQyIBW3KPjpUi
(2, 'teacher1', 0x7ad61b1db1fef10352abaa67634dfb072f98cbb581b4632c46cacfdca70a06d8, 'Test Teacher 1'), -- ruPmE5tCQyIBW3KPjpUi
(11, 'testtest', 0x37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578, 'testtest'); -- testtest

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answer`
--
ALTER TABLE `answer`
 ADD PRIMARY KEY (`id`), ADD KEY `question_id` (`question_id`), ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `assignment`
--
ALTER TABLE `assignment`
 ADD PRIMARY KEY (`id`), ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
 ADD PRIMARY KEY (`id`), ADD KEY `instructor_id` (`instructor_id`), ADD KEY `instructor_id_2` (`instructor_id`);

--
-- Indexes for table `enrollment`
--
ALTER TABLE `enrollment`
 ADD PRIMARY KEY (`course_id`,`user_id`), ADD KEY `course_id` (`course_id`), ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
 ADD PRIMARY KEY (`id`), ADD KEY `student_id` (`student_id`), ADD KEY `instructor_id` (`instructor_id`), ADD KEY `question_id` (`question_id`), ADD KEY `assignment_id` (`assignment_id`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
 ADD PRIMARY KEY (`id`), ADD KEY `assignment_id` (`assignment_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answer`
--
ALTER TABLE `answer`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `assignment`
--
ALTER TABLE `assignment`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=12;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `answer`
--
ALTER TABLE `answer`
ADD CONSTRAINT `answer_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
ADD CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `assignment`
--
ALTER TABLE `assignment`
ADD CONSTRAINT `assignment_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `course`
--
ALTER TABLE `course`
ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`instructor_id`) REFERENCES `user` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `enrollment`
--
ALTER TABLE `enrollment`
ADD CONSTRAINT `enrollment_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
ADD CONSTRAINT `enrollment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `message`
--
ALTER TABLE `message`
ADD CONSTRAINT `message_ibfk_4` FOREIGN KEY (`assignment_id`) REFERENCES `assignment` (`id`) ON DELETE CASCADE,
ADD CONSTRAINT `message_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
ADD CONSTRAINT `message_ibfk_2` FOREIGN KEY (`instructor_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
ADD CONSTRAINT `message_ibfk_3` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `question`
--
ALTER TABLE `question`
ADD CONSTRAINT `question_ibfk_1` FOREIGN KEY (`assignment_id`) REFERENCES `assignment` (`id`) ON DELETE CASCADE;

