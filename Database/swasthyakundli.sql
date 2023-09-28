-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 28, 2023 at 05:56 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `swasthyakundli`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `user_id` int(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `mobile_no` int(15) NOT NULL,
  `dob` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`user_id`, `name`, `email`, `password`, `mobile_no`, `dob`) VALUES
(1001, 'pradeep saini', 'admin@gmail.com', 'admin', 972121212, '2023-09-27');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `user_id` int(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `mobile_no` int(15) NOT NULL,
  `dob` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`user_id`, `name`, `email`, `password`, `mobile_no`, `dob`) VALUES
(2001, 'Dr. Pradeep', 'doctor@gmail.com', 'doctor', 873827382, '2023-09-13'),
(2002, 'Dr. Ram', 'ram@gmail.com', 'ram', 8732838, '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `partnership`
--

CREATE TABLE `partnership` (
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobile` int(16) NOT NULL,
  `type` varchar(10) NOT NULL,
  `message` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `partnership`
--

INSERT INTO `partnership` (`name`, `email`, `mobile`, `type`, `message`) VALUES
('None', 'None', 0, 'None', 'None');

-- --------------------------------------------------------

--
-- Table structure for table `patient_record`
--

CREATE TABLE `patient_record` (
  `user_id` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `date` varchar(15) NOT NULL,
  `report_desc` varchar(500) DEFAULT NULL,
  `doctor_precp` varchar(500) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `img_path` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_record`
--

INSERT INTO `patient_record` (`user_id`, `name`, `date`, `report_desc`, `doctor_precp`, `status`, `img_path`) VALUES
('101', 'X-ray', '2023-09-07', 'Sustained multiple rib fractures and a pneumothorax (collapsed lung) in a fall. He underwent surgery to stabilize the \r\nfractures and treat the pneumothorax.\r\n', ' Prescribed pain medication, recommended chest physiotherapy, and advised close monitoring for lung recovery.', 'Warning', '/static/images/Reports/pradeep saini/4994014ef5c834e4803541aa1dc874_jumbo.jpeg'),
('101', 'Itpcr', '1222-09-09', ' tested positive for COVID-19 after experiencing symptoms such as fever, cough, and shortness of breath. She is currently in isolation and receiving medical care.', ' Prescribed antiviral medications, oxygen therapy, and advised isolation until she tests negative for the virus.', 'Warning', '/static/images/Reports/pradeep sainiperson1_bacteria_2.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `mobile_no` int(15) NOT NULL,
  `dob` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `name`, `email`, `password`, `mobile_no`, `dob`) VALUES
(101, 'pradeep saini', 'user@gmail.com', 'user', 922222222, NULL),
(105, 'Lakshay', 'Lakshay@gmail.com', 'Lakshay', 34343434, '0000-00-00'),
(106, 'Dr. Lakshay', 'lak@gmail.com', 'lak', 89898989, '0000-00-00'),
(107, 'Vinay Kumar', 'vinay@gmail.com', 'vinay', 952112200, '0000-00-00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `user_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1002;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `user_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2005;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=108;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
