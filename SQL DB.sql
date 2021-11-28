create user SGBDD identified by 123;
grant create session to sgbdd;
grant dba to sgbdd;

conn sgbdd/123@xepdb1


------------------------------CREACION DE TIPOS------------------------------
CREATE OR REPLACE TYPE producto_obj AS OBJECT(
	nombre VARCHAR2(50),
 	precio NUMBER(5,2)
	);
	/


------------------------------CREACION DE TABLAS------------------------------
CREATE TABLE categoria(
	id_categoria INT,
	nombre_categoria VARCHAR2(30) NOT NULL,
	descripcion_categoria VARCHAR2(50),
	CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
	);

CREATE TABLE marca(
	id_marca INT, 
	nombre_marca VARCHAR2(30) NOT NULL,
	CONSTRAINT pk_marca PRIMARY KEY (id_marca)
	);

CREATE TABLE producto(
	id_producto INT,
	prod producto_obj NOT NULL,
	stock INT,  
	id_categoria INT,
	id_marca INT,
	CONSTRAINT pk_producto PRIMARY KEY (id_producto),
	CONSTRAINT fk_producto_categoria FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria),
 	CONSTRAINT fk_producto_marca FOREIGN KEY (id_marca) REFERENCES marca(id_marca), 
	CONSTRAINT ck_producto_stock_positivo CHECK(stock >= 0),
	CONSTRAINT ck_producto_precio_positivo CHECK(prod.precio >= 0)
	);

CREATE TABLE modo_pago(
 	id_modo_pago INT,
	nombre_modo_pago VARCHAR2(20) NOT NULL,
	detalles_modo_pago VARCHAR2(30),
	CONSTRAINT pk_modo_pago PRIMARY KEY (id_modo_pago)
	);

CREATE TABLE cliente(
	id_cliente INT UNIQUE, 
	email_cliente VARCHAR2(50) UNIQUE,
	nombre_cliente VARCHAR2(40) NOT NULL,
	apellido_cliente VARCHAR2(50) NOT NULL, 
	telefono_cliente NUMBER(10),
	CONSTRAINT pk_cliente PRIMARY KEY (id_cliente, email_cliente)
	);

CREATE TABLE factura(
	id_factura INT,
	id_cliente INT NOT NULL,
	fecha_factura DATE NOT NULL,
	id_modo_pago INT NOT NULl,
	CONSTRAINT pk_factura PRIMARY KEY (id_factura),
	CONSTRAINT fk_factura_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
	CONSTRAINT fk_factura_modo_pago FOREIGN KEY (id_modo_pago) REFERENCES modo_pago(id_modo_pago)
	);

CREATE TABLE detalle(
	id_detalle INT,
	id_factura INT,
	id_producto INT,
	cantidad_detalle INT, 
	precio_detalle NUMBER (5,2),
	CONSTRAINT pk_detalle PRIMARY KEY (id_detalle, id_factura),
	CONSTRAINT fk_detalle_producto FOREIGN KEY (id_producto) REFERENCES producto(id_producto),
	CONSTRAINT ck_cantidad_precio_detalle_positivo CHECK(cantidad_detalle > 0 AND precio_detalle > 0)
	);

CREATE TABLE transacciones(
	id_transaccion NUMBER,
	tabla VARCHAR2(255),
	tipo_transaccion VARCHAR2(10),
	usuario VARCHAR2(30),
	fecha_transaccion DATE,
	CONSTRAINT pk_transacciones PRIMARY KEY (id_transaccion)
	);

CREATE TABLE historial_producto(
	id_producto INT,
	fecha_modificacion DATE,
	prod_anterior producto_obj,
	prod_nuevo producto_obj,
	CONSTRAINT fk_transacciones FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
	);

------------------------------CREACION DE VISTAS------------------------------
CREATE OR REPLACE VIEW vista_producto AS 
	SELECT p.id_producto, p.prod, p.stock, m.nombre_marca, c.nombre_categoria
	FROM producto p, marca m, categoria c
	WHERE p.id_marca = m.id_marca
	AND p.id_categoria = c.id_categoria;

CREATE OR REPLACE VIEW vista_factura AS
	SELECT f.id_factura, f.fecha_factura, c.nombre_cliente, c.apellido_cliente, mp.nombre_modo_pago
	FROM factura f, cliente c, modo_pago mp
	WHERE f.id_cliente = c.id_cliente
	AND f.id_modo_pago = mp.id_modo_pago; 

CREATE OR REPLACE VIEW vista_detalle AS
	SELECT d.id_factura, p.prod, d.cantidad_detalle, d.precio_detalle
	FROM detalle d, producto p, factura f
	WHERE d.id_factura = f.id_factura
	AND d.id_producto = p.id_producto;


------------------------------CREACION DE PAQUETE------------------------------
CREATE OR REPLACE PACKAGE altas AS
	PROCEDURE a_categoria(	id 			categoria.id_categoria%type, 
							nombre 		categoria.nombre_categoria%type, 
							descripcion categoria.descripcion_categoria%type);

	PROCEDURE a_marca(	id 		marca.id_marca%type,
						nombre	marca.nombre_marca%type);

	PROCEDURE a_producto(	id 			producto.id_producto%type,
							nom_prod	producto.prod.nombre%type,
							prec_prod	producto.prod.precio%type,
							stock		producto.stock%type,
							id_cat		producto.id_categoria%type,
							id_mar		producto.id_marca%type);

	PROCEDURE a_modo_pago(	id		modo_pago.id_modo_pago%type,
							nombre	modo_pago.nombre_modo_pago%type,
							detalle	modo_pago.detalles_modo_pago%type);
	
	PROCEDURE a_cliente(	id 			cliente.id_cliente%type, 
							email		cliente.email_cliente%type,
							nombre		cliente.nombre_cliente%type,
							apellido	cliente.apellido_cliente%type, 
							tel			cliente.telefono_cliente%type);

	PROCEDURE a_factura(	id_fac	factura.id_factura%type,
							id_cli	factura.id_cliente%type,
							fecha	factura.fecha_factura%type,
							id_mp	factura.id_modo_pago%type);

	PROCEDURE a_detalle(	id_det	detalle.id_detalle%type,
							id_fac	detalle.id_factura%type,
							id_prod	detalle.id_producto%type,
							cant	detalle.cantidad_detalle%type, 
							prec	detalle.precio_detalle%type);
	END altas;
	/

CREATE OR REPLACE PACKAGE BODY altas AS
	PROCEDURE a_categoria(	id 			categoria.id_categoria%type, 
							nombre 		categoria.nombre_categoria%type,
							descripcion	categoria.descripcion_categoria%type) 
		IS
		BEGIN
			INSERT INTO categoria (id_categoria, nombre_categoria, descripcion_categoria) 
				VALUES(id, nombre, descripcion);
		END a_categoria;


	PROCEDURE a_marca(	id 		marca.id_marca%type,
						nombre	marca.nombre_marca%type)
		IS
		BEGIN
			INSERT INTO marca (id_marca, nombre_marca) 
				VALUES(id, nombre);
		END a_marca;


	PROCEDURE a_producto(	id 			producto.id_producto%type,
							nom_prod	producto.prod.nombre%type,
							prec_prod	producto.prod.precio%type,
							stock		producto.stock%type,
							id_cat		producto.id_categoria%type,
							id_mar		producto.id_marca%type)
		IS
		BEGIN
			INSERT INTO producto (id_producto, prod, stock, id_categoria, id_marca)
			VALUES (id, producto_obj(nom_prod, prec_prod), stock, id_cat, id_mar);
		END a_producto;


	PROCEDURE a_modo_pago(	id		modo_pago.id_modo_pago%type,
							nombre	modo_pago.nombre_modo_pago%type,
							detalle	modo_pago.detalles_modo_pago%type)
		IS
		BEGIN
			INSERT INTO modo_pago (id_modo_pago, nombre_modo_pago, detalles_modo_pago)
			VALUES (id, nombre, detalle);
		END a_modo_pago;


	PROCEDURE a_cliente(	id 			cliente.id_cliente%type, 
							email		cliente.email_cliente%type,
							nombre		cliente.nombre_cliente%type,
							apellido	cliente.apellido_cliente%type, 
							tel			cliente.telefono_cliente%type)
		IS
		BEGIN
			INSERT INTO cliente (id_cliente, email_cliente, nombre_cliente, apellido_cliente, telefono_cliente)
			VALUES (id, email, nombre, apellido, tel);
		END a_cliente;


	PROCEDURE a_factura(	id_fac	factura.id_factura%type,
							id_cli	factura.id_cliente%type,
							fecha	factura.fecha_factura%type,
							id_mp	factura.id_modo_pago%type)
		IS
		BEGIN
			INSERT INTO factura (id_factura, id_cliente, fecha_factura, id_modo_pago)
			VALUES (id_fac, id_cli, fecha, id_mp);
		END a_factura;


	PROCEDURE a_detalle(	id_det	detalle.id_detalle%type,
							id_fac	detalle.id_factura%type,
							id_prod	detalle.id_producto%type,
							cant	detalle.cantidad_detalle%type, 
							prec	detalle.precio_detalle%type)
		IS
		BEGIN
			INSERT INTO detalle (id_detalle, id_factura, id_producto, cantidad_detalle, precio_detalle)
			VALUES (id_det, id_fac, id_prod, cant, prec);
		END a_detalle;
	END altas;
	/


------------------------------CREACION DE PROCEDIMIENTOS------------------------------
CREATE OR REPLACE PROCEDURE alta_categoria(	id 		categoria.id_categoria%type, 
						nombre 		categoria.nombre_categoria%type,
						descripcion	categoria.descripcion_categoria%type)
	IS
	BEGIN
		altas.a_categoria(id, nombre, descripcion);
	END alta_categoria;
	/

CREATE OR REPLACE PROCEDURE alta_marca(	id 		marca.id_marca%type,
										nombre	marca.nombre_marca%type)
	IS
	BEGIN
		altas.a_marca(id, nombre);
	END alta_marca;
	/

CREATE OR REPLACE PROCEDURE alta_producto(	id 			producto.id_producto%type,
											nom_prod	producto.prod.nombre%type,
											prec_prod	producto.prod.precio%type,
											stock		producto.stock%type,
											id_cat		producto.id_categoria%type,
											id_mar		producto.id_marca%type)
	IS
	BEGIN
		altas.a_producto(id, nom_prod, prec_prod, stock, id_cat, id_mar);
	END alta_producto;
	/

CREATE OR REPLACE PROCEDURE alta_modo_pago(	id		modo_pago.id_modo_pago%type,
											nombre	modo_pago.nombre_modo_pago%type,
											detalle	modo_pago.detalles_modo_pago%type)
	IS
	BEGIN
		altas.a_modo_pago(id, nombre, detalle);
	END alta_modo_pago;
	/

CREATE OR REPLACE PROCEDURE alta_cliente(	id 			cliente.id_cliente%type, 
											email		cliente.email_cliente%type,
											nombre		cliente.nombre_cliente%type,
											apellido	cliente.apellido_cliente%type, 
											tel			cliente.telefono_cliente%type)
	IS
	BEGIN
		altas.a_cliente(id, email, nombre, apellido, tel);
	END alta_cliente;
	/

CREATE OR REPLACE PROCEDURE alta_factura(	id_fac	factura.id_factura%type,
											id_cli	factura.id_cliente%type,
											fecha	factura.fecha_factura%type,
											id_mp	factura.id_modo_pago%type)
	IS
	BEGIN
		altas.a_factura(id_fac, id_cli, fecha, id_mp);
	END alta_factura;
	/

CREATE OR REPLACE PROCEDURE alta_detalle(	id_det	detalle.id_detalle%type,
											id_fac	detalle.id_factura%type,
											id_prod	detalle.id_producto%type,
											cant	detalle.cantidad_detalle%type, 
											prec	detalle.precio_detalle%type)
	IS
	BEGIN
		altas.a_detalle(id_det, id_fac, id_prod, cant, prec);
	END alta_detalle;
	/


------------------------------CREACION DE INDICES------------------------------
CREATE INDEX indx_producto ON producto(stock);
CREATE INDEX indx_cliente ON cliente(nombre_cliente, apellido_cliente);
CREATE INDEX indx_historial_producto ON historial_producto(id_producto, fecha_modificacion);


------------------------------CREACION DE SECUENCIAS------------------------------
CREATE SEQUENCE seq_categoria
	START WITH 1
	INCREMENT BY 1;

CREATE SEQUENCE seq_marca
	START WITH 1
	INCREMENT BY 1;

CREATE SEQUENCE seq_producto
	START WITH 1
	INCREMENT BY 1;

CREATE SEQUENCE seq_modo_pago
	START WITH 1
	INCREMENT BY 1;

CREATE SEQUENCE seq_cliente
	START WITH 1
	INCREMENT BY 1;

CREATE SEQUENCE seq_factura
	START WITH 1
	INCREMENT BY 1;

CREATE SEQUENCE seq_detalle
	START WITH 1
	INCREMENT BY 1;

CREATE SEQUENCE seq_transacciones
	START WITH 1
	INCREMENT BY 1;


------------------------------CREACION DE TRIGGERS------------------------------
CREATE OR REPLACE TRIGGER trg_transacciones
    AFTER UPDATE OR DELETE ON producto FOR EACH ROW    
	DECLARE
	   l_transaction VARCHAR2(10);
	BEGIN
	   l_transaction := CASE  
	         WHEN UPDATING THEN 'UPDATE'
	         WHEN DELETING THEN 'DELETE'
	   END;
 
	   INSERT INTO sgbdd.transacciones (id_transaccion,	tabla, tipo_transaccion, usuario, fecha_transaccion)
	   VALUES(seq_transacciones.nextval,'PRODUCTO', l_transaction, USER, SYSDATE);
	END;
	/

CREATE OR REPLACE TRIGGER trg_productos
	BEFORE UPDATE ON producto FOR EACH ROW 
	BEGIN
		IF :new.prod.precio <> :old.prod.precio THEN
			INSERT INTO historial_producto(id_producto, fecha_modificacion, prod_anterior, prod_nuevo)
				VALUES (:old.id_producto, SYSDATE, :old.prod, :new.prod);
		END IF;
	END;
	/


------------------------------CREACION DE PERFILES------------------------------
CREATE PROFILE perf_admin LIMIT IDLE_TIME 20;
CREATE PROFILE perf_empleado LIMIT IDLE_TIME 10;
CREATE PROFILE perf_cliente LIMIT IDLE_TIME 5;


------------------------------CREACION DE ROLES------------------------------
CREATE ROLE rol_administrador;
CREATE ROLE rol_empleado;
CREATE ROLE rol_cliente;


------------------------------PERMISOS DE ROLES------------------------------
-----------------ADMINISTRADOR
GRANT CREATE SESSION TO rol_administrador;
GRANT EXECUTE ON SGBDD.producto_obj TO rol_administrador;
GRANT SELECT, UPDATE, INSERT, DELETE ON SGBDD.marca TO rol_administrador;
GRANT SELECT, UPDATE, INSERT, DELETE ON SGBDD.categoria	TO rol_administrador;
GRANT SELECT, UPDATE, INSERT, DELETE ON SGBDD.producto TO rol_administrador;
GRANT SELECT, UPDATE, INSERT, DELETE ON SGBDD.modo_pago TO rol_administrador;
GRANT SELECT, UPDATE, INSERT, DELETE ON SGBDD.cliente TO rol_administrador;
GRANT SELECT, UPDATE, INSERT, DELETE ON SGBDD.factura TO rol_administrador;
GRANT SELECT, UPDATE, INSERT, DELETE ON SGBDD.detalle TO rol_administrador;
GRANT SELECT ON SGBDD.transacciones TO rol_administrador;
GRANT SELECT ON SGBDD.historial_producto TO rol_administrador;
GRANT SELECT ON SGBDD.vista_producto TO rol_administrador;
GRANT SELECT ON SGBDD.vista_factura TO rol_administrador;
GRANT SELECT ON SGBDD.vista_detalle TO rol_administrador;
GRANT EXECUTE ON SGBDD.alta_marca TO rol_administrador;
GRANT EXECUTE ON SGBDD.alta_categoria TO rol_administrador;
GRANT EXECUTE ON SGBDD.alta_producto TO rol_administrador;
GRANT EXECUTE ON SGBDD.alta_modo_pago TO rol_administrador;
GRANT EXECUTE ON SGBDD.alta_cliente TO rol_administrador;
GRANT EXECUTE ON SGBDD.alta_factura TO rol_administrador;
GRANT EXECUTE ON SGBDD.alta_detalle TO rol_administrador;

-----------------EMPLEADO
GRANT CREATE SESSION TO rol_empleado;
GRANT EXECUTE ON SGBDD.producto_obj TO rol_empleado;
GRANT SELECT ON SGBDD.marca TO rol_empleado;
GRANT SELECT ON SGBDD.categoria	TO rol_empleado;
GRANT SELECT ON SGBDD.modo_pago TO rol_empleado;
GRANT SELECT, UPDATE, INSERT ON SGBDD.producto TO rol_empleado;
GRANT SELECT, UPDATE, INSERT ON SGBDD.cliente TO rol_empleado;
GRANT SELECT, UPDATE, INSERT ON SGBDD.factura TO rol_empleado;
GRANT SELECT, UPDATE, INSERT ON SGBDD.detalle TO rol_empleado;
GRANT SELECT ON SGBDD.transacciones TO rol_empleado;
GRANT SELECT ON SGBDD.vista_producto TO rol_empleado;
GRANT SELECT ON SGBDD.vista_factura TO rol_empleado;
GRANT SELECT ON SGBDD.vista_detalle TO rol_empleado;
GRANT EXECUTE ON SGBDD.alta_marca TO rol_empleado;
GRANT EXECUTE ON SGBDD.alta_categoria TO rol_empleado;
GRANT EXECUTE ON SGBDD.alta_producto TO rol_empleado;
GRANT EXECUTE ON SGBDD.alta_cliente TO rol_empleado;
GRANT EXECUTE ON SGBDD.alta_factura TO rol_empleado;
GRANT EXECUTE ON SGBDD.alta_detalle TO rol_empleado;

-----------------CLIENTE
GRANT CREATE SESSION TO rol_cliente;
GRANT EXECUTE ON SGBDD.producto_obj TO rol_cliente;
GRANT SELECT ON SGBDD.marca TO rol_cliente;
GRANT SELECT ON SGBDD.categoria	TO rol_cliente;
GRANT SELECT ON SGBDD.producto TO rol_cliente;
GRANT SELECT ON SGBDD.modo_pago TO rol_cliente;
GRANT SELECT, INSERT ON SGBDD.factura TO rol_cliente;
GRANT SELECT, INSERT ON SGBDD.detalle TO rol_cliente;
GRANT SELECT ON SGBDD.vista_producto TO rol_cliente;
GRANT SELECT ON SGBDD.vista_factura TO rol_cliente;
GRANT SELECT ON SGBDD.vista_detalle TO rol_cliente;
GRANT EXECUTE ON SGBDD.alta_factura TO rol_cliente;
GRANT EXECUTE ON SGBDD.alta_detalle TO rol_cliente;


------------------------------CREACION DE USUARIOS------------------------------
CREATE USER usr_administrador IDENTIFIED BY 123 PROFILE perf_admin;
CREATE USER usr_empleado IDENTIFIED BY 123 PROFILE perf_empleado;
CREATE USER usr_cliente IDENTIFIED BY 123 PROFILE perf_cliente;

GRANT rol_administrador TO usr_administrador;
GRANT rol_empleado TO usr_empleado;
GRANT rol_cliente TO usr_cliente;