create database pupil; 
use pupil;
create table pupil_details(
pupil_id int not null,
fullname varchar (20) not null,
age decimal (3,1),
sen varchar (20) not null,
fsm varchar (20) not null,
primary key (pupil_id),
unique (pupil_id)
);
Insert into pupil_details (pupil_id, fullname, age, sen, fsm)
Values ('1', 'Sarah', '11.4', 'Yes', 'Yes'),
('2', 'James', '12.0', 'No', 'Yes'),
('3', 'Joy', '12.6', 'No', 'No'),
('4', 'Kath', '12.2', 'No', 'No');
explain pupil_details;
Select * from pupil_details;
CREATE TABLE pupil_scores(
pupil_id int not null,
maths int not null,
English int not null,
primary key (pupil_id),
Unique (pupil_id)
);
Insert into pupil_scores (pupil_id, maths, english)
Values ('1', '68', '78'), 
 ('2', '78', '54'),
 ('3', '54', '88'),
 ('4', '60', '65');
 select * from pupil_scores;
 explain pupil_scores;
 
select pupil_scores.pupil_id, pupil_details.pupil_id
From pupil_scores
Inner join pupil_details
On pupil_scores. pupil_id = pupil_details. pupil_id;  

SELECT*FROM pupil_scores WHERE maths = '68';

SELECT*FROM pupil_scores, pupil_details
WHERE pupil_scores.pupil_id =  pupil_details.pupil_id AND pupil_scores.maths = '68';

Select * from pupil_scores
Where English between 70 and 100;

Select * from pupil_details
Where age between 12.0 and 13.0;













