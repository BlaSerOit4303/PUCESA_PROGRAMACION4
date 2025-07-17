-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: CURRENT_TIMESTAMP
-- Server version: 8.0.30
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
 /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
 /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 /*!40101 SET NAMES utf8mb4 */;

-- 
-- Database: `flask_mysql_4to_1po2025`
-- 

-- --------------------------------------------------------

--
-- Table structure for table `cuenta_usuario`
--

CREATE TABLE `cuenta_usuario` (
  `id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `nombre_completo` varchar(100) NOT NULL,
  `email` varchar(120) DEFAULT NULL,
  `rol` enum('admin','usuario') NOT NULL DEFAULT 'usuario',
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cuenta_usuario`
--

INSERT INTO `cuenta_usuario` (`id`, `username`, `password_hash`, `nombre_completo`, `email`, `rol`) VALUES
(1, 'admin', 'HASH_ADMIN_PASSWORD', 'Administrador Principal', 'admin@admin.com', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `curso`
--

CREATE TABLE `curso` (
  `id` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `creador_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--Crear tabla Provincias
CREATE TABLE provincias (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL UNIQUE
);
--Crear tabla rutas
CREATE TABLE rutas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  origen_id INT NOT NULL,
  destino_id INT NOT NULL,
  costo INT NOT NULL,
  FOREIGN KEY (origen_id) REFERENCES provincias(id) ON DELETE CASCADE,
  FOREIGN KEY (destino_id) REFERENCES provincias(id) ON DELETE CASCADE
);
--
-- Dumping data for table `curso`
--

INSERT INTO `curso` (`id`, `nombre`, `descripcion`, `creador_id`) VALUES
(1, 'Sistemas de la Información - Programación 4', 'Profesor: Edison Menéses. Curso de programación avanzada con Python y Flask.', 1);

--
-- Indexes for dumped tables
--

-- Indexes for table `cuenta_usuario`
ALTER TABLE `cuenta_usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

-- Indexes for table `curso`
ALTER TABLE `curso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `creador_id` (`creador_id`);

--
-- AUTO_INCREMENT for dumped tables
--

-- AUTO_INCREMENT for table `cuenta_usuario`
ALTER TABLE `cuenta_usuario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

-- AUTO_INCREMENT for table `curso`
ALTER TABLE `curso`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

-- Constraints for table `curso`
ALTER TABLE `curso`
  ADD CONSTRAINT `curso_ibfk_1` FOREIGN KEY (`creador_id`) REFERENCES `cuenta_usuario` (`id`) ON DELETE SET NULL;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
 /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
 /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

⚠️ Notas importantes
- Reemplaza 'HASH_ADMIN_PASSWORD' con la salida real de generate_password_hash('123') desde Flask.
- Esta estructura está alineada con tu app actual, modelo CuentaUsuario, y controlador de cursos.
- Puedes exportar este bloque como .sql y cargarlo directamente desde phpMyAdmin o vía consola.
from flask import render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash