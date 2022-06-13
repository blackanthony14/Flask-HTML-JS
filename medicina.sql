-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 13, 2022 at 09:51 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `basemedica`
--

-- --------------------------------------------------------

--
-- Table structure for table `medicina`
--

DROP TABLE IF EXISTS `medicina`;
CREATE TABLE IF NOT EXISTS `medicina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(500) NOT NULL,
  `apellido` varchar(500) NOT NULL,
  `direccion` varchar(500) NOT NULL,
  `numeroTele` int(11) NOT NULL,
  `edad` varchar(500) NOT NULL,
  `peso` varchar(500) NOT NULL,
  `altura` varchar(500) NOT NULL,
  `enfermedades` varchar(500) NOT NULL,
  `medicacion` varchar(500) NOT NULL,
  `condiciones` varchar(500) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicina`
--

INSERT INTO `medicina` (`id`, `nombre`, `apellido`, `direccion`, `numeroTele`, `edad`, `peso`, `altura`, `enfermedades`, `medicacion`, `condiciones`, `fecha`) VALUES
(1, 'ksjdb', 'kajhfbka', 'khabsdk', 34545, 'iuaefiebf', 'iadbid', 'iaebfisf', 'iaebfif', 'iubhdib', 'jhesbfkbf', '2022-06-13 07:28:59'),
(2, 'Raydel A', 'W', 'San Miguel', 3545, '22', '78 kg', '1.78 m', 'Asma, Dosplasia Medular', 'Ninguna', 'Ninguna', '2022-06-13 00:00:00'),
(3, 'Raydel A', 'W', 'San Miguel', 3545, '22', '78 kg', '1.78 m', 'Asma, Dosplasia Medular', 'Ninguna', 'Ninguna', '2022-06-13 00:00:00'),
(4, 'Dodo', 'Dodi', 'Coseva', 2223122, '19', '70kg', '1.65m', 'Asma, Dosplasia Medular', 'Acetominofen', 'Ninguna', '2022-06-13 00:00:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
