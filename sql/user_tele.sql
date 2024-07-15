-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 15, 2024 at 05:42 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `telegram`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_tele`
--

CREATE TABLE `user_tele` (
  `id_tele` int(11) NOT NULL,
  `id_user_tele` varchar(500) NOT NULL,
  `username_user_tele` varchar(500) NOT NULL,
  `nama_user_tele` varchar(500) NOT NULL,
  `notif_user_tele` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_tele`
--

INSERT INTO `user_tele` (`id_tele`, `id_user_tele`, `username_user_tele`, `nama_user_tele`, `notif_user_tele`) VALUES
(11, '5878006277', 'dlixpro', 'Code is Life', 'nonaktif');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_tele`
--
ALTER TABLE `user_tele`
  ADD PRIMARY KEY (`id_tele`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_tele`
--
ALTER TABLE `user_tele`
  MODIFY `id_tele` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
