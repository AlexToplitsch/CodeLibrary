-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 03. Nov 2020 um 13:03
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
-- Tabellenstruktur für Tabelle `apprentice_list`
--

CREATE TABLE `apprentice_list` (
  `Personalnummer` int(11) NOT NULL,
  `Vorname` text NOT NULL,
  `Nachname` text NOT NULL,
  `Geburtsdatum` date NOT NULL,
  `Geschlecht` text NOT NULL,
  `Lehrberuf` text NOT NULL,
  `Hauptmodul` text NOT NULL,
  `Spezialmodul` text NOT NULL,
  `Lehrbeginn` date NOT NULL,
  `Lehrdauer` text NOT NULL,
  `Mail` text NOT NULL,
  `Telefonnummer` text NOT NULL,
  `Strasse` text NOT NULL,
  `Hausnummer` text NOT NULL,
  `PLZ` text NOT NULL,
  `ORT` text NOT NULL,
  `LKZ` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `apprentice_list`
--

INSERT INTO `apprentice_list` (`Personalnummer`, `Vorname`, `Nachname`, `Geburtsdatum`, `Geschlecht`, `Lehrberuf`, `Hauptmodul`, `Spezialmodul`, `Lehrbeginn`, `Lehrdauer`, `Mail`, `Telefonnummer`, `Strasse`, `Hausnummer`, `PLZ`, `ORT`, `LKZ`) VALUES
(23423, 'Lorenz ', 'Mühlehner', '2000-01-03', 'männlich', '', '', '', '2000-01-03', '0', '', '', '', '', '', '', ''),
(243424, 'adasd', 'asdas', '2000-01-01', 'männlich', '', '', '', '2000-01-01', '0', '', '', '', '', '', '', ''),
(436634, 'ADSWAS', 'SADSAD', '2000-01-01', 'männlich', '', '', '', '2000-01-01', '0', '', '', '', '', '', '', '');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `apprentice_list`
--
ALTER TABLE `apprentice_list`
  ADD PRIMARY KEY (`Personalnummer`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
