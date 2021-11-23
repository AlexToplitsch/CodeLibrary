-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 12. Nov 2020 um 15:58
-- Server-Version: 10.4.14-MariaDB
-- PHP-Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `apprentice_management_system`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `apprentice_fachgebiete`
--

CREATE TABLE `apprentice_fachgebiete` (
  `Fachgebiet` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `apprentice_fachgebiete`
--

INSERT INTO `apprentice_fachgebiete` (`Fachgebiet`) VALUES
('Fachrechnen'),
('Fachzeichnen'),
('Grundlagen IT'),
('Maschinenelemente'),
('Werkstoffkunde');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `apprentice_fachgebiete`
--
ALTER TABLE `apprentice_fachgebiete`
  ADD PRIMARY KEY (`Fachgebiet`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
