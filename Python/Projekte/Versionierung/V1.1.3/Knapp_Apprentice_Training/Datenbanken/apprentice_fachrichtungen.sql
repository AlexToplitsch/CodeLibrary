-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 19. Nov 2020 um 15:08
-- Server-Version: 10.4.14-MariaDB
-- PHP-Version: 7.2.34

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
-- Tabellenstruktur für Tabelle `apprentice_fachrichtungen`
--

CREATE TABLE `apprentice_fachrichtungen` (
  `Fachrichtung` varchar(10) NOT NULL,
  `Bezeichnung` varchar(30) NOT NULL,
  `Lehrjahre` float NOT NULL,
  `Benutzername` varchar(30) NOT NULL,
  `Aenderungsdatum` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `apprentice_fachrichtungen`
--

INSERT INTO `apprentice_fachrichtungen` (`Fachrichtung`, `Bezeichnung`, `Lehrjahre`, `Benutzername`, `Aenderungsdatum`) VALUES
('APP', 'Applikationsentwickler', 4, 'root', '2020-11-19 13:58:38'),
('MB', 'Maschinenbau', 3.5, 'root', '2020-11-19 13:47:14'),
('ME', 'Mechatroniker', 3.5, 'root', '2020-11-19 13:32:42');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `apprentice_fachrichtungen`
--
ALTER TABLE `apprentice_fachrichtungen`
  ADD PRIMARY KEY (`Fachrichtung`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
