use Music_Database;
create table Artist(
name text,
genre text,
image_link text,
bio text
);
create table Album(
title text,
artist text,
genre text,
art text
);
create table Track(
number int,
title text,
artist text,
album text,
duration text
);
