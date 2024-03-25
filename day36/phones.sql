-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3606
-- Généré le : jeu. 12 mai 2022 à 03:26
-- Version du serveur :  5.7.30
-- Version de PHP : 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `PhonesDB`
--

-- --------------------------------------------------------

--
-- Structure de la table `Phones`
--

CREATE TABLE IF NOT EXISTS `Phones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `owner` varchar(255) NOT NULL,
  `price` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `comment` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `Phones`
--

INSERT INTO `Phones` (`id`, `model`, `brand`, `owner`, `price`, `weight`, `comment`) VALUES
(1, 'iphoneX', 'Apple', 'Terry', 100, 174, 'No scratches brand new state'),
(2, 'G10', 'Huawei ', 'Brad', 150, 164, 'old phone from my mom good deal'),
(3, '9 PureView', 'Nokia  ', 'Stacy', 50, 172, 'loved that phone'),
(4, 'P99', 'Panasonic', 'Brad', 75, 145, 'good deal low price'),
(5, 'A7 XL', 'alcatel ', 'Stacy', 20, 175, 'the screen resoltion is nice not too heavy'),
(6, 'K8 Plus', 'Lenovo ', 'Richard', 80, 165, 'good a new phone don\'t need that one'),
(7, 'Xperia XZ1', 'Sony', 'Brad', 60, 155, 'Always been a fan on this phone very convenient'),
(8, 'Galaxy A8+ (2018)', 'Samsung', 'Alex', 90, 191, 'heavy but good phone'),
(9, 'Z3', 'Sharp', 'Alex', 120, 185, 'sharp like a knife haha'),
(10, 'Q8 (2017)', 'LG', 'Stacy', 30, 146, 'good opportunity'),
(11, 'Mi A1 (Mi 5X)', 'Xiaomi', 'Stacy', 50, 146, 'basic xiaomi light'),
(12, 'nubia M2 lite', 'ZTE', 'Brad', 30, 164, 'lighter than air :)'),
(13, 'Sense 50x', 'Archos', 'Richard', 70, 223, 'my wife\'s phone she doesn\'t need it anymore '),
(14, 'Pixel 2', 'Google', 'Roland', 80, 143, 'perfect for teens'),
(15, 'Moto E4 Plus', 'Motorola', 'Roland', 90, 198, 'never got it wrong with motorola'),
(16, 'Aurora', 'BlackBerry', 'Stacy', 200, 178, 'vintage'),
(17, 'Pixel XL', 'Google', 'Frank', 100, 168, 'the best google phone'),
(18, 'Galaxy S8', 'Samsung', 'Frank', 120, 155, 'Light and practical '),
(19, 'Y5II', 'Huawei', 'Brad', 150, 184, 'good phone'),
(20, 'Xperia X Performance', 'Sony', 'Brad', 100, 164, 'good performance'),
(21, '230 Dual SIM', 'Nokia', 'Frank', 60, 91, 'light dual SIM good for PRO'),
(22, '222 Dual SIM', 'Nokia', 'Frank', 60, 91, 'light dual SIM good for PRO'),
(23, 'Desire 520', 'HTC', 'Richard', 30, 100, 'heh good'),
(24, 'iPhone 6s Plus', 'Apple', 'Stacy', 100, 192, 'basic but still really good for a first phone'),
(25, 'One M9+', 'HTC', 'Victoria', 115, 168, 'basic'),
(26, 'Desire P', 'HTC', 'Victoria', 115, 136, 'basic'),
(27, 'Desire 700 dual sim', 'HTC', 'Victoria', 115, 149, 'basic DUAL'),
(28, '108 Dual SIM', 'Nokia', 'Victoria', 35, 70, 'basic DUAL'),
(29, 'Butterfly', 'HTC', 'Victoria', 95, 140, 'like the name'),
(30, 'Desire SV', 'HTC', 'Victoria', 45, 131, 'like the name'),
(31, 'Galaxy A02', 'Samsung', 'Stacy', 45, 206, 'good samsung phone'),
(32, '1.4', 'Nokia', 'Vincent', 200, 178, 'my favorite Nokia'),
(33, 'Mate X2', 'Huawei', 'Vincent', 150, 295, 'find your mate mate'),
(34, 'Desire 21 Pro 5G', 'HTC', 'Vincent', 350, 295, 'finally 5g'),
(35, 'Galaxy S21+ 5G', 'Samsung', 'Alex', 350, 169, 'the best'),
(36, '5.4', 'Nokia', 'Alex', 350, 181, 'very good for a nokia'),
(37, 'Wildfire E', 'HTC', 'Alex', 150, 160, 'wild one'),
(38, 'Moto G Stylus (2021)', 'Motorola', 'Alex', 160, 213, 'stylus system'),
(39, 'iPhone 12 mini', 'Apple', 'Stacy', 660, 135, 'tiny but awesome'),
(40, 'Galaxy S20 FE', 'Samsung', 'Nina', 360, 190, 'sell my old phone'),
(41, 'K31', 'LG', 'Nina', 160, 146, 'dad\'s old phone'),
(42, 'Xperia 5 II', 'Sony', 'Nina', 180, 163, 'mom\'s old phone'),
(43, 'Velvet 5G UW', 'LG', 'Nina', 210, 193, 'sis old phone'),
(44, 'Galaxy Note20 Ultra', 'Samsung', 'Nina', 310, 208, 'bro old phone'),
(45, 'Galaxy Note20', 'Samsung', 'Alex', 300, 192, 'good phone sad to sell it');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;