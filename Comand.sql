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


INSERT INTO us00rs_cr4sh3d (nombreUsuario, email, password,ip,deviceName,RolUserMainCreate) VALUES
('th3Ghostface', 'mopch891@gmail.com', '032003', '197.0.0.1','CashFucker','gh')