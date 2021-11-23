-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 19. Nov 2020 um 15:11
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
-- Tabellenstruktur für Tabelle `apprentice_ausbilder`
--

CREATE TABLE `apprentice_ausbilder` (
  `id` int(11) NOT NULL,
  `Familienname` varchar(50) NOT NULL,
  `Vorname` varchar(30) NOT NULL,
  `Telefon` varchar(20) NOT NULL,
  `Wochenstunden` int(11) NOT NULL,
  `Eintrittsdatum` varchar(10) NOT NULL,
  `Austrittsdatum` varchar(10) NOT NULL,
  `wt_mo` tinyint(1) NOT NULL,
  `wt_di` tinyint(1) NOT NULL,
  `wt_mi` tinyint(1) NOT NULL,
  `wt_do` tinyint(1) NOT NULL,
  `wt_fr` tinyint(1) NOT NULL,
  `Benutzer` varchar(80) NOT NULL,
  `Änderung` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `apprentice_ausbilder`
--
ALTER TABLE `apprentice_ausbilder`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `apprentice_ausbilder`
--
ALTER TABLE `apprentice_ausbilder`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
