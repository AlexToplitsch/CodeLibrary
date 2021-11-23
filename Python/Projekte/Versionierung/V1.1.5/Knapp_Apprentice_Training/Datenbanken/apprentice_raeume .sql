-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 19. Nov 2020 um 14:55
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
-- Tabellenstruktur für Tabelle `apprentice_raeume`
--

CREATE TABLE `apprentice_raeume` (
  `Raum` varchar(25) NOT NULL,
  `Gebäude` varchar(25) NOT NULL,
  `Stock` int(11) NOT NULL,
  `RaumNr` varchar(25) NOT NULL,
  `Plätze` varchar(25) NOT NULL,
  `Benutzer` varchar(41) NOT NULL,
  `Änderung` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `apprentice_raeume`
--

INSERT INTO `apprentice_raeume` (`Raum`, `Gebäude`, `Stock`, `RaumNr`, `Plätze`, `Benutzer`, `Änderung`) VALUES
('Lehrsaal 1', 'B8', 0, '', '', 'sd', '2020-11-19 13:27:10'),
('Lehrsaal2', 'B8', 1, '', '', 'root', '2020-11-19 13:28:33'),
('Lehrwerkstatt', 'H16', 0, '', '', '', '2020-11-19 13:12:29'),
('Ötscher', 'H16', 1, '', '', '', '2020-11-19 13:12:29'),
('Schöckl', 'H16', 1, '', '', '', '2020-11-19 13:12:29'),
('Semmering', 'H16', 1, '', '', '', '2020-11-19 13:12:29'),
('Sozialraum', 'H16', 1, '', '', '', '2020-11-19 13:12:29');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `apprentice_raeume`
--
ALTER TABLE `apprentice_raeume`
  ADD PRIMARY KEY (`Raum`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
