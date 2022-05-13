create database dbshop;

create table t_product(
title varchar (500) primary key,
url  varchar(500) ,
img varchar(500),
price varchar(100)
);
create table t_shop(
Id int primary key auto_increment,
name varchar(200),
ActivityBasin varchar(200),
link varchar(200),
MaduleName varchar(200),
Conditions varchar(100)
);
create table temp_shop(
name varchar(200) primary key,
ActivityBasin varchar(200),
link varchar(200)
 
);
create table t_role(
  roleId int primary key ,
  roleTitle varchar(100) not null
);

create table t_user(
      userId int primary key  auto_increment,
      name varchar(100),
      family varchar(100),
      userName varchar(100),
      password varchar(100),
      role_Id int,
      foreign key (role_Id) references t_role(roleId)
);

