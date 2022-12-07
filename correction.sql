/*
tableNames=['uber', 'dono_do_carro', 'owner', 'driver']
pkNames=['id', 'placa', 'rg']
pkTypes=['char','integer', 'bigint']
pkHasCompose=True
fkNames=[]
fkTypes=[]
*/
CREATE TABLE motorista
(
  cpf text not null,
  primary key(cpf)
);

/*
tableNames=['car', 'auto', 'vehicle', 'automovel']
pkNames=[]
fkNames=['owner']
fkTypes=['varchar varying']
*/
CREATE TABLE carro
(
  id text not null,
  placa char(7) not null,
  modelo varchar(20) not null,
  dono text not null,
  primary key(placa),
  foreign key (dono) references motorista(cpf)
);
