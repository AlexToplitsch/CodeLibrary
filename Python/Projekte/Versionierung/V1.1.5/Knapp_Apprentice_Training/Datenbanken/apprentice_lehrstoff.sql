-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 19. Nov 2020 um 15:12
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
-- Tabellenstruktur für Tabelle `apprentice_lehrstoff`
--

CREATE TABLE `apprentice_lehrstoff` (
  `id` int(11) NOT NULL,
  `Fachgebiet` varchar(30) NOT NULL,
  `LehrstoffID` varchar(30) NOT NULL,
  `Verantwortlicher` varchar(50) NOT NULL,
  `Bezeichnung` varchar(50) NOT NULL,
  `Dokument` varchar(50) NOT NULL,
  `Stunden` int(11) NOT NULL,
  `Hilfsmittel` varchar(50) NOT NULL,
  `Benutzer` varchar(30) NOT NULL,
  `Änderung` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `apprentice_lehrstoff`
--

INSERT INTO `apprentice_lehrstoff` (`id`, `Fachgebiet`, `LehrstoffID`, `Verantwortlicher`, `Bezeichnung`, `Dokument`, `Stunden`, `Hilfsmittel`, `Benutzer`, `Änderung`) VALUES
(24, 'Fachrechnen', '', 'Abdelnaim', '', '(\'D:/Python/LAB Verwaltung/Excel-Dateien/Übersicht', 0, '', 'root', '2020-11-19 13:22:46');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `apprentice_lehrstoff`
--
ALTER TABLE `apprentice_lehrstoff`
  ADD PRIMARY KEY (`id`,`Fachgebiet`,`LehrstoffID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `apprentice_lehrstoff`
--
ALTER TABLE `apprentice_lehrstoff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
