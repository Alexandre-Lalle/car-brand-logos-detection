-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2023 at 07:59 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_brand_logos`
--

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

CREATE TABLE `cars` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `country` varchar(200) NOT NULL,
  `year` varchar(200) NOT NULL,
  `company` varchar(200) NOT NULL,
  `logo` varchar(200) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`id`, `name`, `country`, `year`, `company`, `logo`, `description`) VALUES
(1, 'toyota', 'Japan', '1937', 'Toyota Motor Corporation', './car_brands/toyota.png', 'Toyota Motor Corporation est un constructeur automobile multinational japonais fondé en 1937. Toyota est l\'un des plus grands constructeurs automobiles au monde et est connue pour ses technologies innovantes, telles que les véhicules hybrides et à pile à combustible. Toyota produit une large gamme de véhicules, des voitures compactes aux camions et VUS.'),
(2, 'mazda', 'Japan', '1920', 'Mazda Motor Corporation', './car_brands/mazda.png', 'Mazda Motor Corporation est une société automobile japonaise fondée en 1920. Mazda est connue pour son ingénierie et sa conception uniques, axées sur la création d\'expériences de conduite agréables. Mazda produit une gamme de véhicules, allant des voitures compactes aux SUV et aux voitures de sport, et participe également au développement de technologies innovantes telles que les moteurs SkyActiv et le moteur rotatif.'),
(3, 'mercedes', 'Germany', '1926', 'Daimler AG', './car_brands/mercedes.jpg', 'Mercedes-Benz est une marque automobile de luxe allemande fondée en 1926. Connue pour ses véhicules haut de gamme, Mercedes est réputée pour la qualité, le confort et l\'innovation. L\'entreprise produit une gamme de voitures, des voitures compactes aux berlines de luxe et aux SUV, ainsi que des véhicules utilitaires comme les bus et les camions.'),
(4, 'volkswagen', 'Germany', '1937', 'Volkswagen Group', './car_brands/volkswagen.png', 'Volkswagen est une marque automobile allemande fondée en 1937. C\'est l\'un des plus grands constructeurs automobiles au monde et produit une gamme de véhicules comprenant des voitures, des camionnettes et des camions. Volkswagen est connu pour son ingénierie de haute qualité et ses conceptions innovantes, et a une forte présence mondiale.\nModèles : Golf, Jetta, Passat, Tiguan, Atlas, Beetle, Polo, Touareg, etc.'),
(5, 'hyundai', 'South Korea', '1967', 'Hyundai Motor Company', './car_brands/hyundai.jpg', 'Hyundai exploite la plus grande usine de fabrication automobile intégrée au monde à Ulsan, en Corée du Sud, qui a une capacité de production annuelle de 1,6 million d\'unités.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cars`
--
ALTER TABLE `cars`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
