CREATE TABLE motorista
(
  id text not null,
  primary key(id)
);

CREATE TABLE car
(
  id text not null,
  placa char(7) not null,
  modelo varchar(20) not null,
  dono text not null,
  primary key(placa),
  foreign key (dono) references motorista(id)
);


