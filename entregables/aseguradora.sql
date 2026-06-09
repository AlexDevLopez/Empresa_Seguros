    CREATE DATABASE IF NOT EXISTS aseguradora
    CHARACTER SET UTF8MB4 COLLATE UTF8MB4_GENERAL_CI;
    USE aseguradora;

    CREATE TABLE Clientes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellidos VARCHAR(80) NOT NULL,
        fecha_nacimiento DATE,
        sexo ENUM('M','F'),
        curp VARCHAR(18) UNIQUE,
        telefono VARCHAR(10),
        correo VARCHAR(100) UNIQUE,
        ocupacion VARCHAR(50),
        ingreso_mensual DECIMAL(10, 2)
    );

    CREATE TABLE Polizas(
        id INT AUTO_INCREMENT PRIMARY KEY,
        numero_poliza INT UNIQUE NOT NULL,
        fecha_inicio DATE,
        fecha_fin DATE,
        prima_mensual DECIMAL(10,2),
        suma_asegurada DECIMAL(10,2),
        tipo_poliza VARCHAR(50),
        estatus VARCHAR(20),
        cliente_id INT,
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
    );

    CREATE TABLE Beneficiarios(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellidos VARCHAR(80) NOT NULL,
        fecha_nacimiento DATE,
        parentesco VARCHAR(50),
        porcentaje_asignado DECIMAL(10,2),
        poliza_id INT,
        FOREIGN KEY (poliza_id) REFERENCES Polizas(id)
    );

    CREATE TABLE Pagos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha_pago DATE,
        monto_pagado DECIMAL(10,2),
        metodo_pago VARCHAR(20),
        referencia VARCHAR(50),
        poliza_id INT,
        FOREIGN KEY (poliza_id) REFERENCES Polizas(id)
    );

    CREATE TABLE Siniestros(
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha_reporte DATE,
        fecha_ocurrencia DATE,
        tipo_siniestro VARCHAR(50),
        monto_reclamado DECIMAL(10,2),
        monto_aprobado DECIMAL(10,2),
        estatus_siniestro ENUM('Pendiente','En Revision','Aprobado','Rechazado'),
        poliza_id INT,
        FOREIGN KEY (poliza_id) REFERENCES Polizas(id)
    );