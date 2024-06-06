CREATE DATABASE IF NOT EXISTS proyectopython;
USE proyectopython;

CREATE TABLE usuarios(
    id          int auto_increment not null,
    nombre      varchar(100),
    apellido    varchar(100),
    email       varchar(100) not null,
    password    varchar(100) not null,
    fecha       date not null,
    CONSTRAINT  pk_usuarios PRIMARY KEY(id),
    CONSTRAINT  uq_email UNIQUE(email)
) ENGINE = InnoDB;

CREATE TABLE notas(
    id          int auto_increment not null,
    usuario_id  int not null,
    titulo      varchar(255),
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT  pk_notas PRIMARY KEY(id),
    CONSTRAINT  fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
) ENGINE = InnoDB;