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
-- Tabellenstruktur für Tabelle `apprentice_lap_themenkatalog`
--

CREATE TABLE `apprentice_lap_themenkatalog` (
  `id` int(11) NOT NULL,
  `Fachrichtung` varchar(50) NOT NULL,
  `Themen_ID` varchar(50) NOT NULL,
  `Thema` varchar(200) NOT NULL,
  `Ausbilder` varchar(100) NOT NULL,
  `Lehrjahr` int(11) NOT NULL,
  `BS_Lehrjahr` int(11) NOT NULL,
  `Benutzer` varchar(50) NOT NULL,
  `Änderung` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `apprentice_lap_themenkatalog`
--

INSERT INTO `apprentice_lap_themenkatalog` (`id`, `Fachrichtung`, `Themen_ID`, `Thema`, `Ausbilder`, `Lehrjahr`, `BS_Lehrjahr`, `Benutzer`, `Änderung`) VALUES
(1, 'Applikationsentwicklung-Coding', '1.1', 'Kenntnis des Zeichensatzes ASCII', 'Quantschnig', 1, 0, 'user', '0000-00-00 00:00:00'),
(2, 'Applikationsentwicklung-Coding', '1.2', 'Kenntnis der Einheiten Bit, Byte', 'Quantschnig', 1, 0, 'root', '0000-00-00 00:00:00'),
(3, 'Applikationsentwicklung-Coding', '1.3', 'Kenntnis der Begriffe Gigabyte, Terabyte, Petabyte, Exabyte', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(4, 'Applikationsentwicklung-Coding', '1.4', 'Kenntnis der Begriffe Gibibyte, Tebibyte, Pebibyte, Exbibyte', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(5, 'Applikationsentwicklung-Coding', '1.5', 'Kenntnis der gebräuchlichen Zahlensysteme in der IT', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(6, 'Applikationsentwicklung-Coding', '1.6', 'Umwandlung zwischen Binär-, Dezimal- und Hexadezimalzahlen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(7, 'Applikationsentwicklung-Coding', '1.7', 'Kenntnis der Logik-Schaltungen (AND, OR, XOR, NOT) und deren Wahrheitstabellen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(9, 'Applikationsentwicklung-Coding', '2', ' Betriebssysteme und Software', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(10, 'Applikationsentwicklung-Coding', '2.1', 'Fachbegriff Betriebssystem', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(11, 'Applikationsentwicklung-Coding', '2.2', 'Kenntnis der am Markt führend verbreiteten Betriebssysteme', 'Quantschnig', 1, 0, 'root', '0000-00-00 00:00:00'),
(12, 'Applikationsentwicklung-Coding', '2.3', 'Kenntnisse über Desktop-Betriebssysteme', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(13, 'Applikationsentwicklung-Coding', '2.4', 'Fachbegriff Firmware', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(14, 'Applikationsentwicklung-Coding', '2.5', 'Fachbegriffe Systemprogramm, Anwendungsprogramm', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(14, 'Maschinenbau', '1.1.1', 'Zerspanen', '', 3, 3, '', '0000-00-00 00:00:00'),
(15, 'Applikationsentwicklung-Coding', '2.6', 'Fachbegriff Multitasking-Betriebssystem', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(16, 'Applikationsentwicklung-Coding', '2.7', 'Fachbegriffe Single-User-System, Multi-User-System', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(17, 'Applikationsentwicklung-Coding', '2.8', 'Kenntnis über die Powershell (inkl. einfacher Befehle)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(18, 'Applikationsentwicklung-Coding', '2.9', 'Kenntnisse über grafische Oberflächen unter Linux', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(19, 'Applikationsentwicklung-Coding', '2.10', 'Fachbegriff Dateisystem', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(21, 'Applikationsentwicklung-Coding', '3', 'Betreuung von mobiler Hardware', '', 0, 0, '', '0000-00-00 00:00:00'),
(22, 'Applikationsentwicklung-Coding', '3.1', 'Technische Merkmale von Smartphones', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(23, 'Applikationsentwicklung-Coding', '3.2', 'Technische Merkmale von Tablets', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(24, 'Applikationsentwicklung-Coding', '3.3', 'Kenntnisse über Android', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(25, 'Applikationsentwicklung-Coding', '3.4', 'Kenntnisse über IOS', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(26, 'Applikationsentwicklung-Coding', '3.5', 'Fachbegriff QR-Code', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(27, 'Applikationsentwicklung-Coding', '3.6', 'Vor- und Nachteile von geschlossenen Systemen mit Betriebssystem und App-Store', '', 0, 0, '', '0000-00-00 00:00:00'),
(29, 'Applikationsentwicklung-Coding', '4', 'Technische Dokumentationen/Projektarbeit/Schulungen', '', 0, 0, '', '0000-00-00 00:00:00'),
(30, 'Applikationsentwicklung-Coding', '4.1', 'Aufgabe und Strukturierung von Testläufen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(31, 'Applikationsentwicklung-Coding', '4.2', 'Protokollieren technischer Arbeiten', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(32, 'Applikationsentwicklung-Coding', '4.3', 'Inhalt einer technischen Dokumentation/technisches Protokoll (z.B. FAQ, …)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(33, 'Applikationsentwicklung-Coding', '4.4', 'Aufbereitung einer technischen Dokumentation/technisches Protokoll', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(34, 'Applikationsentwicklung-Coding', '4.5', 'Kenntnis über Abläufe und Prozessschritte zum Roll-out von Applikationen (z.B. Einführungsvorgehen, Sicherheitsanforderungen, \r\nevtl. Abbruch und Rückführung, Datenmigration/Konvertierung, Anwendersch', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(35, 'Applikationsentwicklung-Coding', '4.6', 'Gestaltung und Vorbereitung von Präsentationen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(37, 'Applikationsentwicklung-Coding', '5', 'Gesetzliche Bestimmungen im Zusammenhang mit Applikationsentwicklung – Coding', '', 0, 0, '', '0000-00-00 00:00:00'),
(38, 'Applikationsentwicklung-Coding', '5.1', 'Kenntnis über DSGVO (Datenschutzgrundverordnung)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(39, 'Applikationsentwicklung-Coding', '5.2', 'Fachbetriff \"Datenminimierung\" im Zusammenhang der DSGVO', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(40, 'Applikationsentwicklung-Coding', '5.3', 'Fachbegriffe \"betroffene Personen\", Verantwortlicher, Auftragsverarbeiter', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(41, 'Applikationsentwicklung-Coding', '5.4', 'Kenntnis über Rechte von \"betroffene Personen\" lt. DSGVO', '', 0, 0, '', '0000-00-00 00:00:00'),
(42, 'Applikationsentwicklung-Coding', '5.5', 'Fachbegriff \"personenbezogene und sensible Daten\" lt. DSGVO', '', 0, 0, '', '0000-00-00 00:00:00'),
(43, 'Applikationsentwicklung-Coding', '5.6', 'Bedeutung von Kopplungsverbot beim DSGVO', '', 0, 0, '', '0000-00-00 00:00:00'),
(44, 'Applikationsentwicklung-Coding', '5.7', 'Datenschutzbeauftragter lt. DSGVO und dessen Funktion', '', 0, 0, '', '0000-00-00 00:00:00'),
(45, 'Applikationsentwicklung-Coding', '5.8', 'Pflichten für Unternehmen bei bekannt gewordenen Datendiebstahl lt. DSGVO', '', 0, 0, '', '0000-00-00 00:00:00'),
(46, 'Applikationsentwicklung-Coding', '5.9', 'Kenntnisse über Grundbegriffe und Gültigkeitsbereich des Urheberrechtes', '', 0, 0, '', '0000-00-00 00:00:00'),
(47, 'Applikationsentwicklung-Coding', '5.10', 'Kenntnis gesetzlicher Gewährleistungs- und Garantiebestimmungen und deren \r\nunterschiedlicher Anwendung bei Hardware- und Softwareproblemen', '', 0, 0, '', '0000-00-00 00:00:00'),
(48, 'Applikationsentwicklung-Coding', '5.11', 'Kenntnisse über umweltgerechte Entsorgung von Elektronikschrott, Toner, Akkus oder Batterien', '', 0, 0, '', '0000-00-00 00:00:00'),
(49, 'Applikationsentwicklung-Coding', '5.12', 'Kenntnisse über das E-Commerce-Gesetz (ECG)', '', 0, 0, '', '0000-00-00 00:00:00'),
(50, 'Applikationsentwicklung-Coding', '5.13', 'Kenntnisse über das Telekom-Gesetz (TKG)', '', 0, 0, '', '0000-00-00 00:00:00'),
(51, 'Applikationsentwicklung-Coding', '5.14', 'Kenntnisse über Pflichtangaben eines Homepage-Betreibers (Impressum)', '', 0, 0, '', '0000-00-00 00:00:00'),
(52, 'Applikationsentwicklung-Coding', '5.15', 'Kenntnisse über Pflichtangaben beim E-Mail-Verkehr von Unternehmen', '', 0, 0, '', '0000-00-00 00:00:00'),
(53, 'Applikationsentwicklung-Coding', '5.16', 'Kenntnisse über die gesetzliche Einhaltung von Bildschirmpausen', '', 0, 0, '', '0000-00-00 00:00:00'),
(55, 'Applikationsentwicklung-Coding', '6', 'Netzwerkdienste', '', 0, 0, '', '0000-00-00 00:00:00'),
(56, 'Applikationsentwicklung-Coding', '6.1', 'Fachbegriffe Domain, Sub-Domain und Top-Level-Domain', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(57, 'Applikationsentwicklung-Coding', '6.2', 'Kenntnis der Web-Protokolle HTTP und HTTPS', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(58, 'Applikationsentwicklung-Coding', '6.3', 'Funktionsprinzip eines Mail-Servers', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(59, 'Applikationsentwicklung-Coding', '6.4', 'Kenntnis des Mail-Protokolls POP3/POP3S', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(60, 'Applikationsentwicklung-Coding', '6.5', 'Kenntnis des Mail-Protokolls IMAP/IMAPS', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(61, 'Applikationsentwicklung-Coding', '6.6', 'Kenntnis des Mail-Protokolls SMTP/SMTPS', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(62, 'Applikationsentwicklung-Coding', '6.7', 'Kenntnisse über FTP/FTPS', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(63, 'Applikationsentwicklung-Coding', '6.8', 'Kenntnisse über SSL', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(64, 'Applikationsentwicklung-Coding', '6.9', 'Fachbegriff Cloud-Computing', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(65, 'Applikationsentwicklung-Coding', '6.10', 'Kenntnisse über Private/Public/Hybrid Cloud', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(66, 'Applikationsentwicklung-Coding', '6.11', 'Fachbegriffe IaaS, PaaS, SaaS', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(67, 'Applikationsentwicklung-Coding', '6.12', 'Beispiele für marktbekannte Cloud-Dienste', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(68, 'Applikationsentwicklung-Coding', '6.13', 'Kriterien und Voraussetzungen für den Einsatz von Cloud-Diensten', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(70, 'Applikationsentwicklung-Coding', '7', 'IT-Security und Betriebssicherheit', '', 0, 0, '', '0000-00-00 00:00:00'),
(71, 'Applikationsentwicklung-Coding', '7.1', 'Kenntnisse über Gefahren von Viren, Würmern, Trojanern, Spyware, Hackern und Phishing', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(72, 'Applikationsentwicklung-Coding', '7.2', 'Fachbegriff Zero-Day-Exploit', '', 0, 0, '', '0000-00-00 00:00:00'),
(73, 'Applikationsentwicklung-Coding', '7.3', 'Kenntnisse über Einschränkungsmöglichkeiten bei Benutzerkonten', '', 0, 0, '', '0000-00-00 00:00:00'),
(74, 'Applikationsentwicklung-Coding', '7.4', 'Funktion einer Software-Firewall', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(75, 'Applikationsentwicklung-Coding', '7.5', 'Kenntnisse über Möglichkeiten Client-PCs vor Missbrauch zu schützen', '', 0, 0, '', '0000-00-00 00:00:00'),
(76, 'Applikationsentwicklung-Coding', '7.6', 'Kenntnisse über sichere Planung von Backups', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(77, 'Applikationsentwicklung-Coding', '7.7', 'Kenntnisse über verschiedene Backup-Prinzipien', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(78, 'Applikationsentwicklung-Coding', '7.8', 'Kenntnisse über Backup-Medien und deren richtiger Lagerung', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(80, 'Applikationsentwicklung-Coding', '8', 'Informatik und Gesellschaft', '', 0, 0, '', '0000-00-00 00:00:00'),
(81, 'Applikationsentwicklung-Coding', '8.1', 'Fachbegriff Big-Data', '', 0, 0, '', '0000-00-00 00:00:00'),
(82, 'Applikationsentwicklung-Coding', '8.2', 'Fachbegriff Web 2.0', '', 0, 0, '', '0000-00-00 00:00:00'),
(83, 'Applikationsentwicklung-Coding', '8.3', 'Fachbegriff Industrie 4.0', '', 0, 0, '', '0000-00-00 00:00:00'),
(84, 'Applikationsentwicklung-Coding', '8.4', 'Fachbegriff IoT', '', 0, 0, '', '0000-00-00 00:00:00'),
(85, 'Applikationsentwicklung-Coding', '8.5', 'Kenntnisse über Vor- und Nachteile bei Nutzung von Sprachassistenten', '', 0, 0, '', '0000-00-00 00:00:00'),
(86, 'Applikationsentwicklung-Coding', '8.6', 'Kenntnisse über e-Government, digitale Signatur und Handy-Signatur', '', 0, 0, '', '0000-00-00 00:00:00'),
(87, 'Applikationsentwicklung-Coding', '8.7', 'Schutzmöglichkeiten vor Cookie-Tracking und Cookieless-Tracking', '', 0, 0, '', '0000-00-00 00:00:00'),
(88, 'Applikationsentwicklung-Coding', '8.8', 'Kenntnisse über die Gefahr von Identitätsdiebstahl', '', 0, 0, '', '0000-00-00 00:00:00'),
(89, 'Applikationsentwicklung-Coding', '8.9', 'Fachbegriff Netzneutralität', '', 0, 0, '', '0000-00-00 00:00:00'),
(90, 'Applikationsentwicklung-Coding', '8.10', 'Kenntnisse über Vor- und Nachteile bei Nutzung von biometrischen Daten', '', 0, 0, '', '0000-00-00 00:00:00'),
(91, 'Applikationsentwicklung-Coding', '8.11', 'Inhalte von Unternehmensrichtlinien für Nutzung von sozialen Netzwerken', '', 0, 0, '', '0000-00-00 00:00:00'),
(93, 'Applikationsentwicklung-Coding', '9', 'Ergonomische Gestaltung eines Arbeitsplatzes', '', 0, 0, '', '0000-00-00 00:00:00'),
(94, 'Applikationsentwicklung-Coding', '9.1', 'Kenntnisse über die ergonomische Einrichtung eines Bildschirmarbeitsplatzes', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(95, 'Applikationsentwicklung-Coding', '9.2', 'Kenntnisse über den optimalen Aufstellungsort von Bildschirmen (Lichteinfall)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(96, 'Applikationsentwicklung-Coding', '9.3', 'Kenntnisse der gesetzlichen Bestimmungen von Pausen bei Bildschirmarbeit', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(97, 'Applikationsentwicklung-Coding', '9.4', 'Kenntnisse über die ideale Höhe von Tisch/Tastatur, Bildschirmoberkante und Bildschirmabstand zum Benutzer', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(98, 'Applikationsentwicklung-Coding', '9.5', 'Kenntnisse über Schutzmaßnahmen zur Vorbeugung körperlicher Schäden bei sitzender Tätigkeit', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(99, 'Applikationsentwicklung-Coding', '9.6', 'Kenntnisse über körperliche Entspannungsübungen bei sitzender Tätigkeit', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(101, 'Applikationsentwicklung-Coding', '10', 'Fachberatung, Planung', '', 0, 0, '', '0000-00-00 00:00:00'),
(102, 'Applikationsentwicklung-Coding', '10.1', 'Führen von fachspezifischen Verkaufsgesprächen, Produktberatung', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(103, 'Applikationsentwicklung-Coding', '10.2', 'Kompetenz, technische Zusammenhänge beratend erklären zu können', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(104, 'Applikationsentwicklung-Coding', '10.3', 'Beratung und Erstellen kundenorientierter Softwarelösungen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(105, 'Applikationsentwicklung-Coding', '10.4', 'Kenntnisse über richtigen Umgang bei Reklamationen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(106, 'Applikationsentwicklung-Coding', '10.5', 'Richtiger Kundenumgang bei folgenreichen technischen Problemen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(108, 'Applikationsentwicklung-Coding', '11', 'Informatik', '', 0, 0, '', '0000-00-00 00:00:00'),
(109, 'Applikationsentwicklung-Coding', '11.1', 'Fachbegriff Informatik', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(110, 'Applikationsentwicklung-Coding', '11.2', 'Typen von Webseiten (statische, dynamische Webseiten)', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(111, 'Applikationsentwicklung-Coding', '11.3', 'Fachbegriffe Weblog, Webshop, Web-Plattform', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(112, 'Applikationsentwicklung-Coding', '11.4', 'Auszeichnungssprachen HTML, XML – Fachbegriff und Einsatzgebiet', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(113, 'Applikationsentwicklung-Coding', '11.5', 'Kenntnisse über das HTML5-Grundgerüst mit den wichtigsten Bestandteilen', '', 0, 0, '', '0000-00-00 00:00:00'),
(114, 'Applikationsentwicklung-Coding', '11.6', 'Fachbegriff Meta-Element/Metadaten', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(115, 'Applikationsentwicklung-Coding', '11.7', 'Fachbegriff SEO und Maßnahmen', '', 0, 0, '', '0000-00-00 00:00:00'),
(116, 'Applikationsentwicklung-Coding', '11.8', 'Fachbegriff Cascading StyleSheets und deren Einsatz', '', 0, 0, '', '0000-00-00 00:00:00'),
(117, 'Applikationsentwicklung-Coding', '11.9', 'Scripting (clientseitiges Scripting, serverseitiges Scripting)', '', 0, 0, '', '0000-00-00 00:00:00'),
(118, 'Applikationsentwicklung-Coding', '11.10', 'Software zum Erstellen und Betrachten von Webseiten (Code-Editoren, Web-Browser, \r\nFTP-Programme, Grafikprogramme, Serversoftware)', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(119, 'Applikationsentwicklung-Coding', '11.11', 'Fachbegriff CMS (Einsatzgebiet, notwendige Voraussetzungen, existierende Systeme am Markt)', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(120, 'Applikationsentwicklung-Coding', '11.12', 'Unterschied LIFO/FIFO-Prinzip', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(121, 'Applikationsentwicklung-Coding', '11.13', 'Fachbegriffe Stack und Queue', '', 0, 0, '', '0000-00-00 00:00:00'),
(122, 'Applikationsentwicklung-Coding', '11.14', 'Fachbegriff Userinterface (Arten, Regeln für Entwurf, Gestaltungshilfen/Toolkits/Frameworks)', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(123, 'Applikationsentwicklung-Coding', '11.15', 'Fachbegriff Zeichencodierung (ASCII, ISO-Latin, Unicode, … – Unterschiede und Verwendung)', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(124, 'Applikationsentwicklung-Coding', '11.16', 'Standards ANSI, ISO, IEEE', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(125, 'Applikationsentwicklung-Coding', '11.17', 'Fachbegriff Frame', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(126, 'Applikationsentwicklung-Coding', '11.18', 'Fachbegriff Webservices (verteiltes System für heterogene Systeme, …)', '', 0, 0, '', '0000-00-00 00:00:00'),
(127, 'Applikationsentwicklung-Coding', '11.19', 'Kenntnisse über Standards (SOAP, WSDL, …)', '', 0, 0, '', '0000-00-00 00:00:00'),
(128, 'Applikationsentwicklung-Coding', '11.20', 'Fachbegriff Rest API', '', 0, 0, '', '0000-00-00 00:00:00'),
(129, 'Applikationsentwicklung-Coding', '11.21', 'Fachbegriff JSON', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(130, 'Applikationsentwicklung-Coding', '11.22', 'Fachbegriff Agile Softwareentwicklung', '', 0, 0, '', '0000-00-00 00:00:00'),
(131, 'Applikationsentwicklung-Coding', '11.23', 'Fachbegriff Reaktive Programmierung', '', 0, 0, '', '0000-00-00 00:00:00'),
(132, 'Applikationsentwicklung-Coding', '11.24', 'Kenntnisse über Frameworks', '', 0, 0, '', '0000-00-00 00:00:00'),
(133, 'Applikationsentwicklung-Coding', '11.25', 'Einsatzgebiete Angular JS', 'Karrer', 0, 0, '', '0000-00-00 00:00:00'),
(134, 'Applikationsentwicklung-Coding', '11.26', 'Einsatzgebiete Bootstrap', 'Karrer', 0, 0, '', '0000-00-00 00:00:00'),
(135, 'Applikationsentwicklung-Coding', '11.27', 'Einsatzgebiet jQuery', '', 0, 0, '', '0000-00-00 00:00:00'),
(136, 'Applikationsentwicklung-Coding', '11.28', 'Kenntnisse über den Zugriff PHP auf mySQL-Datenbank (Dienste Server/Client)', '', 0, 0, '', '0000-00-00 00:00:00'),
(137, 'Applikationsentwicklung-Coding', '11.29', 'Fachbegriff Multitasking', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(138, 'Applikationsentwicklung-Coding', '11.30', 'Kenntnisse über mobile Webseiten/Optimierung für Smartphones', '', 0, 0, '', '0000-00-00 00:00:00'),
(139, 'Applikationsentwicklung-Coding', '11.31', 'Fachbegriff Responsive Webdesign, Umsetzung', '', 0, 0, '', '0000-00-00 00:00:00'),
(140, 'Applikationsentwicklung-Coding', '11.32', 'Kenntnisse über Konzept Mobile First', '', 0, 0, '', '0000-00-00 00:00:00'),
(141, 'Applikationsentwicklung-Coding', '11.33', 'Kenntnisse über aktuelle Programmiersprachen', 'Quantschnig/Karrer', 0, 0, '', '0000-00-00 00:00:00'),
(142, 'Applikationsentwicklung-Coding', '11.34', 'Kenntnisse über Programmiersprachen für mobile Anwendungen/Internet', '', 0, 0, '', '0000-00-00 00:00:00'),
(143, 'Applikationsentwicklung-Coding', '11.35', 'Kenntnisse über die Anwendung von JAVA-Technologien im Web (Servlets, Java-Server-Pages)', 'Karrer', 0, 0, '', '0000-00-00 00:00:00'),
(144, 'Applikationsentwicklung-Coding', '11.36', 'Grundkenntnisse über die Anwendung der .NET-Technologien im Web (ASP.NET)', '', 0, 0, '', '0000-00-00 00:00:00'),
(145, 'Applikationsentwicklung-Coding', '11.37', 'Fachbegriff Metadaten', 'Quantschnig', 0, 0, '', '0000-00-00 00:00:00'),
(146, 'Applikationsentwicklung-Coding', '11.38', 'Prinzipien der Softwareentwicklung: KISS, DRY', '', 0, 0, '', '0000-00-00 00:00:00'),
(147, 'Applikationsentwicklung-Coding', '11.39', 'Kenntnisse über Coding-Standards/Code-Konventionen', '', 0, 0, '', '0000-00-00 00:00:00'),
(148, 'Applikationsentwicklung-Coding', '11.40', 'Fachbegriff Cross Plattform Entwicklung', '', 0, 0, '', '0000-00-00 00:00:00'),
(149, 'Applikationsentwicklung-Coding', '11.41', 'Fachbegriff Corporate Identity (CI)', '', 0, 0, '', '0000-00-00 00:00:00'),
(150, 'Applikationsentwicklung-Coding', '11.42', 'Fachbegriff Corporate Design (CD)', '', 0, 0, '', '0000-00-00 00:00:00'),
(151, 'Applikationsentwicklung-Coding', '11.43', 'CI/CD Vorgaben bei der Applikationsentwicklung', '', 0, 0, '', '0000-00-00 00:00:00'),
(153, 'Applikationsentwicklung-Coding', '12', ' Projektmanagement', '', 0, 0, '', '0000-00-00 00:00:00'),
(154, 'Applikationsentwicklung-Coding', '12.1', 'Fachbegriff Projektmanagement', '', 0, 0, '', '0000-00-00 00:00:00'),
(155, 'Applikationsentwicklung-Coding', '12.2', 'Definition von Projekten', '', 0, 0, '', '0000-00-00 00:00:00'),
(156, 'Applikationsentwicklung-Coding', '12.3', 'Fachbegriff Pflichtenheft und notwendiger Inhalt', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(157, 'Applikationsentwicklung-Coding', '12.4', 'Fachbegriff Lastenheft und notwendiger Inhalt', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(158, 'Applikationsentwicklung-Coding', '12.5', 'Kenntnisse über Spannungsfelder in einem Projekt', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(159, 'Applikationsentwicklung-Coding', '12.6', 'Kenntnisse über den Fachbegriff Primäres Projektziel', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(160, 'Applikationsentwicklung-Coding', '12.7', 'Kenntnisse über Vor- und Nachteile einer Projektorganisation', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(161, 'Applikationsentwicklung-Coding', '12.8', 'Ziel einer Projektdokumentation', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(162, 'Applikationsentwicklung-Coding', '12.9', 'Fachbegriff Struktogramm', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(163, 'Applikationsentwicklung-Coding', '12.10', 'Fachbegriff Ablaufdiagramm (Flowchart)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(164, 'Applikationsentwicklung-Coding', '12.11', 'Kenntnisse über wesentliche Schritte einer Projektplanung', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(165, 'Applikationsentwicklung-Coding', '12.12', 'Kenntnisse über Eigenschaften eines Projektleiters', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(166, 'Applikationsentwicklung-Coding', '12.13', 'Aufgaben eines Projektleiters', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(167, 'Applikationsentwicklung-Coding', '12.14', 'Kenntnisse über Dokumentationen eines Projektes', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(168, 'Applikationsentwicklung-Coding', '12.15', 'Fachbegriff Projektauftrag', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(169, 'Applikationsentwicklung-Coding', '12.16', 'Fachbegriff Projektstrukturplan', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(170, 'Applikationsentwicklung-Coding', '12.17', 'Fachbegriff Arbeitspaket', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(171, 'Applikationsentwicklung-Coding', '12.18', 'Fachbegriff Meilenstein', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(172, 'Applikationsentwicklung-Coding', '12.19', 'Unterschiede internes/externes Projekt', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(173, 'Applikationsentwicklung-Coding', '12.20', 'Kenntnis Projektkostenplanung', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(175, 'Applikationsentwicklung-Coding', '13', 'Projektmethoden, Tools', '', 0, 0, '', '0000-00-00 00:00:00'),
(176, 'Applikationsentwicklung-Coding', '13.1', 'Kenntnisse über Softwareprozessmodelle', '', 0, 0, '', '0000-00-00 00:00:00'),
(177, 'Applikationsentwicklung-Coding', '13.2', 'Kenntnisse über den Aufbau des Wasserfallmodells', '', 0, 0, '', '0000-00-00 00:00:00'),
(178, 'Applikationsentwicklung-Coding', '13.3', 'Kenntnisse über Agiles Projektmanagement/Methoden', '', 0, 0, '', '0000-00-00 00:00:00'),
(179, 'Applikationsentwicklung-Coding', '13.4', 'Fachbegriff DevOps', '', 0, 0, '', '0000-00-00 00:00:00'),
(180, 'Applikationsentwicklung-Coding', '13.5', 'Fachbegriff Scrummaster', '', 0, 0, '', '0000-00-00 00:00:00'),
(181, 'Applikationsentwicklung-Coding', '13.6', 'Fachbegriff Productowner', '', 0, 0, '', '0000-00-00 00:00:00'),
(182, 'Applikationsentwicklung-Coding', '13.7', 'Fachbegriff Backlog', '', 0, 0, '', '0000-00-00 00:00:00'),
(183, 'Applikationsentwicklung-Coding', '13.8', 'Fachbegriff Sprint', '', 0, 0, '', '0000-00-00 00:00:00'),
(184, 'Applikationsentwicklung-Coding', '13.9', 'Fachbegriff Stakeholder', '', 0, 0, '', '0000-00-00 00:00:00'),
(185, 'Applikationsentwicklung-Coding', '13.10', 'Fachbegriff Daily Scrum/Daily Standup', '', 0, 0, '', '0000-00-00 00:00:00'),
(186, 'Applikationsentwicklung-Coding', '13.11', 'Fachbegriff User Story/Story Board', '', 0, 0, '', '0000-00-00 00:00:00'),
(187, 'Applikationsentwicklung-Coding', '13.12', 'Probleme, die beim Wasserfallmodell auftreten können', '', 0, 0, '', '0000-00-00 00:00:00'),
(188, 'Applikationsentwicklung-Coding', '13.13', 'Kenntnisse über den Aufbau des V-Modells', '', 0, 0, '', '0000-00-00 00:00:00'),
(189, 'Applikationsentwicklung-Coding', '13.14', 'Kenntnisse über Vor- und Nachteile des V-Modells', '', 0, 0, '', '0000-00-00 00:00:00'),
(190, 'Applikationsentwicklung-Coding', '13.15', 'Fachbegriff Softwareentwurf', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(191, 'Applikationsentwicklung-Coding', '13.16', 'Fachbegriff Prototyp', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(192, 'Applikationsentwicklung-Coding', '13.17', 'Fachbegriff Soll-Ist-Analyse', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(193, 'Applikationsentwicklung-Coding', '13.18', 'Fachbegriff Versionsverwaltung', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(195, 'Applikationsentwicklung-Coding', '14', 'Qualitätssicherung', '', 0, 0, '', '0000-00-00 00:00:00'),
(196, 'Applikationsentwicklung-Coding', '14.1', 'Kenntnisse über den Zweck von Code-Reviews', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(197, 'Applikationsentwicklung-Coding', '14.2', 'Fachbegriff Schreibtischtest', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(198, 'Applikationsentwicklung-Coding', '14.3', 'Kenntnisse über Black-Box-Test/White-Box-Test, wesentliche Unterschiede', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(199, 'Applikationsentwicklung-Coding', '14.4', 'Kenntnisse über wichtige Qualitätsmerkmale der Softwarefunktionalität', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(200, 'Applikationsentwicklung-Coding', '14.5', 'Kenntnisse über Changemanagement', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(201, 'Applikationsentwicklung-Coding', '14.6', 'Fachbegriff Versionierung und deren Nutzen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(202, 'Applikationsentwicklung-Coding', '14.7', 'Kenntnisse über Problemmanagement', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(204, 'Applikationsentwicklung-Coding', '15', 'Grundkenntnisse des Programmierens', '', 0, 0, '', '0000-00-00 00:00:00'),
(205, 'Applikationsentwicklung-Coding', '15.1', 'Stadien der Softwareentwicklung', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(206, 'Applikationsentwicklung-Coding', '15.2', 'Fachbegriffe Prozedurale Programmierung, Objektorientierte Programmierung, Unterschiede', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(207, 'Applikationsentwicklung-Coding', '15.3', 'Fachbegriff Algorithmus', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(208, 'Applikationsentwicklung-Coding', '15.4', 'Fachbegriff Pseudocode', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(209, 'Applikationsentwicklung-Coding', '15.5', 'Kenntnisse über Sortieralgorithmen (Bubblesort, Quicksort)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(210, 'Applikationsentwicklung-Coding', '15.6', 'Kenntnisse über Suchalgorithmen (sequentielle Suche, binäre Suche)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(211, 'Applikationsentwicklung-Coding', '15.7', 'Ablauf der Programmentwicklung', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(212, 'Applikationsentwicklung-Coding', '15.8', 'Fachbegriffe zum Aufbau einer Programmiersprache \r\n(Syntax, Semantik, Kommentare, Schlüsselwörter, Anweisung)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(213, 'Applikationsentwicklung-Coding', '15.9', 'Fachbegriffe Interpreter und Compiler (Unterschiede, Vor- und Nachteile)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(214, 'Applikationsentwicklung-Coding', '15.10', 'Fachbegriff Debugger (Einsatz)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(215, 'Applikationsentwicklung-Coding', '15.11', 'Fachbegriff Assembler', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(216, 'Applikationsentwicklung-Coding', '15.12', 'Fachbegriff Rekursive Funktionen', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(217, 'Applikationsentwicklung-Coding', '15.13', 'Kenntnisse über ASCII-Tabellen', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(218, 'Applikationsentwicklung-Coding', '15.14', 'Kenntnisse über Variablenarten, Datentypen und Definitionen', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(219, 'Applikationsentwicklung-Coding', '15.15', 'Unterschied Variable und Konstante', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(220, 'Applikationsentwicklung-Coding', '15.16', 'Gültigkeitsbereiche (Lebensdauer) von Variablen', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(221, 'Applikationsentwicklung-Coding', '15.17', 'Fachbegriff Schleifen, Beispiele für Schleifen', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(222, 'Applikationsentwicklung-Coding', '15.18', 'Fachbegriffe \"kopfgesteuert\" bzw. \"fußgesteuert\" im Zusammenhang mit Schleifen', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(223, 'Applikationsentwicklung-Coding', '15.19', 'Kenntnisse über Verzweigungen und Fallunterscheidungen', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(224, 'Applikationsentwicklung-Coding', '15.20', 'Kenntnis der objektorientierten Programmierung (Klassen, Objekte, Vererbung, …)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(226, 'Applikationsentwicklung-Coding', '16', 'Kenntnis und Verwendung von Datenbanken, Datenmodellen und Datenstrukturen', '', 0, 0, '', '0000-00-00 00:00:00'),
(227, 'Applikationsentwicklung-Coding', '16.1', 'Fachbegriff Datenbanksysteme (Traditionelle Datenbanken (RDB), Objektorientierte Datenbanken, \r\nMultimedia-Datenbanken (GIS), Data-Warehouse und OLAP)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(228, 'Applikationsentwicklung-Coding', '16.2', 'Fachbegriffe zu Datenbankabfragen (z.B.: SQL, SQL/XML)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(229, 'Applikationsentwicklung-Coding', '16.3', 'Fachbegriff Datenbankmanagementsystem (DBMS)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(230, 'Applikationsentwicklung-Coding', '16.4', 'Fachbegriff Content Management System (CMS)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(231, 'Applikationsentwicklung-Coding', '16.5', 'Fachbegriff Integrität im Zusammenhang mit Datenbanken', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(232, 'Applikationsentwicklung-Coding', '16.6', 'Fachbegriff Redundanz im Zusammenhang mit Datenbanken', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(233, 'Applikationsentwicklung-Coding', '16.7', 'Vorgangsweise bei der Datenmodellierung (RDB)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(234, 'Applikationsentwicklung-Coding', '16.8', 'Kenntnisse über grundlegende Datenbankoperationen (SELECT, FROM, WHERE, …)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(235, 'Applikationsentwicklung-Coding', '16.9', 'Kenntnisse über die ersten drei Normalformen im Zusammenhang mit Datenbanken', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(236, 'Applikationsentwicklung-Coding', '16.10', 'Fachbegriffe Primärschlüssel, Fremdschlüssel, Relationen', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(237, 'Applikationsentwicklung-Coding', '16.11', 'Kenntnis über Vor- und Nachteile bei Verwendung eines Indexes', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(238, 'Applikationsentwicklung-Coding', '16.12', 'Vor- und Nachteile von Freeware Datenbanken', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(239, 'Applikationsentwicklung-Coding', '16.13', 'Kenntnisse über Sicherungsmethoden', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(240, 'Applikationsentwicklung-Coding', '16.14', 'Fachbegriff Sperrtabelle und Sperrverhalten', '', 0, 0, '', '0000-00-00 00:00:00'),
(241, 'Applikationsentwicklung-Coding', '16.15', 'Fachbegriff BIS (Betriebliches Informationssystem)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(242, 'Applikationsentwicklung-Coding', '16.16', 'Kenntnisse/Fachbegriff ERP Systeme', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(243, 'Applikationsentwicklung-Coding', '16.17', 'Kenntnisse/Fachbegriff BI/BW Systeme', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(244, 'Applikationsentwicklung-Coding', '16.18', 'Kenntnisse der Abläufe und Prozessschritte (Auswählen DBMS, Erstellen des physischen Modells, \r\nPerformance- und Stresstests, Datensicherheit, Datenschutz, \r\nDatenverschlüsselung – Kryptografie, Daten', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(245, 'Applikationsentwicklung-Coding', '16.19', 'Kenntnisse der Abläufe und Prozessschritte (Zugriffsschnittstelle, Zugriffstechnologie, \r\nTransaktionskonzept, Programmierung, Testreihen, Benutzerabnahmetest, Ergebnisprüfung)', 'Quantschnig', 1, 0, '', '0000-00-00 00:00:00'),
(247, 'Applikationsentwicklung-Coding', '17', 'Systementwicklung/Testkonzepte', '', 0, 0, '', '0000-00-00 00:00:00'),
(248, 'Applikationsentwicklung-Coding', '17.1', 'Fachbegriff Programmspezifikation', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(249, 'Applikationsentwicklung-Coding', '17.2', 'Fachbegriff Datenmodell', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(250, 'Applikationsentwicklung-Coding', '17.3', 'Kenntnisse über wichtige Datentypen und Datenstrukturen', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(251, 'Applikationsentwicklung-Coding', '17.4', 'Kenntnisse über Funktionen (Definition, Schnittstelle, Parameter, Rückgabewert, Aufruf)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(252, 'Applikationsentwicklung-Coding', '17.5', 'Unterschiede zwischen Call-By-Value und Call-By-Reference', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(253, 'Applikationsentwicklung-Coding', '17.6', 'Kenntnisse über Klassen (Datenelemente, Konstruktor, Destruktor, Methoden, Zugriffsmodifikatoren)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(254, 'Applikationsentwicklung-Coding', '17.7', 'Kenntnisse über das Prinzip der Vererbung', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(255, 'Applikationsentwicklung-Coding', '17.8', 'Fachbegriff Standardbibliothek', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(256, 'Applikationsentwicklung-Coding', '17.9', 'Kenntnisse über Testkonzepte', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(257, 'Applikationsentwicklung-Coding', '17.10', 'Auswertung eines Softwaretests', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(258, 'Applikationsentwicklung-Coding', '17.11', 'Kriterien für den Test von Datenbankfeldern unterschiedlicher Typen (Mail, Datum, …)', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(259, 'Applikationsentwicklung-Coding', '17.12', 'Unterschiede zwischen einem reproduzierbaren/nicht-reproduzierbaren Fehler', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00'),
(260, 'Applikationsentwicklung-Coding', '17.13', 'Kenntnisse über Möglichkeiten zur Automatisierung von Tests', 'Quantschnig/Karrer', 1, 0, '', '0000-00-00 00:00:00');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `apprentice_lap_themenkatalog`
--
ALTER TABLE `apprentice_lap_themenkatalog`
  ADD PRIMARY KEY (`id`,`Fachrichtung`,`Themen_ID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `apprentice_lap_themenkatalog`
--
ALTER TABLE `apprentice_lap_themenkatalog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=262;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
