select Score , Rank= DENSE_RANK() over (order by Score desc ) from Scores
order by 1 desc 
