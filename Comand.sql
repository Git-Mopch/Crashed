CREATE TABLE us00rs_cr4sh3d (
    id SERIAL PRIMARY KEY,
    nombreUsuario VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL, 
	ip VARCHAR(255) NOT NULL,
	deviceName VARCHAR(255) NOT NULL,
	RolUserMainCreate VARCHAR(2) CHECK (RolUserMainCreate IN ('gt', 'gh', 'bs')), 
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    
);

-- Tabla de sesiones
CREATE TABLE sesiones (
    id SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL REFERENCES us00rs_cr4sh3d(id),
    producto_id INT NOT NULL REFERENCES productos(id),
    esCompra BOOLEAN NOT NULL,
    esVenta BOOLEAN NOT NULL,
    saldoDisponible DECIMAL(10, 2),  -- Campo opcional para saldo disponible
    fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_fin TIMESTAMP
);

-- Tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombreProducto VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    categoria VARCHAR(50)
);

-- Tabla de relación entre productos y sesiones
CREATE TABLE productos_sesion (
    id SERIAL PRIMARY KEY,
    sesion_id INT NOT NULL REFERENCES sesiones(id) ON DELETE CASCADE,
    producto_id INT NOT NULL REFERENCES productos(id) ON DELETE CASCADE,
    cantidad INT DEFAULT 1
);

INSERT INTO us00rs_cr4sh3d (nombreUsuario, email, password,ip,deviceName,RolUserMainCreate) VALUES
('th3Ghostface', 'mopch891@gmail.com', '032003', '197.0.0.1','CashFucker','gh')