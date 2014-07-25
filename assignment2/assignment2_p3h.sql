.mode column
.headers off

----problem 1h
select sum(prod) from (
select x.docid as row_num, y.docid as col_num, (x.count*y.count) as prod from 
(
(select docid, term as xterm, count from frequency) x
join
(select docid, term as yterm, count from frequency) y
)
where xterm=yterm
)
where row_num='10080_txt_crude' and col_num='17035_txt_earn';


--some exploratory analysis: outputs 10 entries in the similarity matrix
select x.docid as row_num, y.docid as col_num, (x.count*y.count) as prod from 
(
(select docid, term as xterm, count from frequency) x
join
(select docid, term as yterm, count from frequency) y
)
where xterm=yterm limit 10;

--shows all common terms and corresponding counts for the docid's referenced in problem 1g
select * from
(select * from frequency where docid='10080_txt_crude') x
join
(select * from frequency where docid='17035_txt_earn') y
on x.term=y.term;
