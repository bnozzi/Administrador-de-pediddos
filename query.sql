CREATE TABLE `proveedores` (
	`razonSocial` text NOT NULL,
	`CUIT` text NOT NULL,
	`CondIVA` text NOT NULL,
	`domicilio` text NOT NULL,
	`localidad` text NOT NULL,
	`telefono` text NOT NULL,
	`fax` text NOT NULL,
	`idPedido` text NOT NULL,
	`idProveedor` int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (`idProveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=Dynamic;

CREATE TABLE `Articulo` (
	`Nombre` text NOT NULL,
	`stock` int NOT NULL,
	`descripcion` text NOT NULL,
	`precioUnitario` int NOT NULL,
	`idArticulo` int NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (`idArticulo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=Dynamic;

CREATE TABLE `pedidos` (
	`idPedido` int NOT NULL AUTO_INCREMENT,
	`idProveedor` int NOT NULL,
	`fecha` date NOT NULL,
	`hora` time NOT NULL,
	`costoTotal` int NOT NULL,
	PRIMARY KEY (`idPedido`),
	KEY `idProveedor` (`idProveedor`),
	CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=Dynamic;

CREATE TABLE `detallePedido` (
	`idDetallePedido` int NOT NULL AUTO_INCREMENT,
	`idArticulo` int NOT NULL,
	`idPedido` int DEFAULT NULL,
	`cantidad` int NOT NULL,
	`subtotal` int NOT NULL,
	`precioUnitario` int NOT NULL,
	PRIMARY KEY (`idDetallePedido`),
	KEY `idArticulo` (`idArticulo`),
	KEY `idPedido` (`idPedido`),
	CONSTRAINT `detallePedido_ibfk_1` FOREIGN KEY (`idArticulo`) REFERENCES `Articulo` (`idArticulo`) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT `detallePedido_ibfk_2` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`idPedido`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=Dynamic;



