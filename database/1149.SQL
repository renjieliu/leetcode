select distinct id = viewer_id  from Views
group by viewer_id,  view_date
having count(distinct article_id) > 1
order by 1 