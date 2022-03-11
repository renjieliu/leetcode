/*
2199. Finding the Topic of Each Post

Table: Keywords

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| topic_id    | int     |
| word        | varchar |
+-------------+---------+
(topic_id, word) is the primary key for this table.
Each row of this table contains the id of a topic and a word that is used to express this topic.
There may be more than one word to express the same topic and one word may be used to express multiple topics.
 

Table: Posts

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| post_id     | int     |
| content     | varchar |
+-------------+---------+
post_id is the primary key for this table.
Each row of this table contains the ID of a post and its content.
Content will consist only of English letters and spaces.
 

Leetcode has collected some posts from its social media website and is interested in finding the topics of each post. Each topic can be expressed by one or more keywords. If a keyword of a certain topic exists in the content of a post (case insensitive) then the post has this topic.

Write an SQL query to find the topics of each post according to the following rules:

If the post does not have keywords from any topic, its topic should be "Ambiguous!".
If the post has at least one keyword of any topic, its topic should be a string of the IDs of its topics sorted in ascending order and separated by commas ','. The string should not contain duplicate IDs.
Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Keywords table:
+----------+----------+
| topic_id | word     |
+----------+----------+
| 1        | handball |
| 1        | football |
| 3        | WAR      |
| 2        | Vaccine  |
+----------+----------+
Posts table:
+---------+------------------------------------------------------------------------+
| post_id | content                                                                |
+---------+------------------------------------------------------------------------+
| 1       | We call it soccer They call it football hahaha                         |
| 2       | Americans prefer basketball while Europeans love handball and football |
| 3       | stop the war and play handball                                         |
| 4       | warning I planted some flowers this morning and then got vaccinated    |
+---------+------------------------------------------------------------------------+
Output: 
+---------+------------+
| post_id | topic      |
+---------+------------+
| 1       | 1          |
| 2       | 1          |
| 3       | 1,3        |
| 4       | Ambiguous! |
+---------+------------+
Explanation: 
1: "We call it soccer They call it football hahaha"
"football" expresses topic 1. There is no other word that expresses any other topic.

2: "Americans prefer basketball while Europeans love handball and football"
"handball" expresses topic 1. "football" expresses topic 1. 
There is no other word that expresses any other topic.

3: "stop the war and play handball"
"war" expresses topic 3. "handball" expresses topic 1.
There is no other word that expresses any other topic.

4: "warning I planted some flowers this morning and then got vaccinated"
There is no word in this sentence that expresses any topic. Note that "warning" is different from "war" although they have a common prefix. 
This post is ambiguous.

Note that it is okay to have one word that expresses more than one topic.


*/


Create table Keywords (topic_id int, word varchar(25))
Create table Posts (post_id int, content varchar(100))
Truncate table Keywords
insert into Keywords (topic_id, word) values ('1', 'handball')
insert into Keywords (topic_id, word) values ('1', 'football')
insert into Keywords (topic_id, word) values ('3', 'WAR')
insert into Keywords (topic_id, word) values ('2', 'Vaccine')
Truncate table Posts
insert into Posts (post_id, content) values ('1', 'We call it soccer They call it football hahaha')
insert into Posts (post_id, content) values ('2', 'Americans prefer basketball while Europeans love handball and football')
insert into Posts (post_id, content) values ('3', 'stop the war and play handball')
insert into Posts (post_id, content) values ('4', 'warning I planted some flowers this morning and then got vaccinated')



--approach 1 with string_split 

/* Write your T-SQL query statement below */
with base as 
(
select 
distinct
p.post_id
, k.topic_id    
from posts p cross apply (select value from string_split(p.content, ' ')) t 
left outer join keywords k
on t.value = k.word
)
select 
post_id
, topic = isnull(string_agg(topic_id, ',') within group (order by cast(topic_id as varchar(20) ) ), 'Ambiguous!')
from base 
group by post_id
order by 1 



/* Write your T-SQL query statement below */

--approach 2 with Like

with base as (
select
distinct 
p.post_id
,topic_id = isnull(cast(k.topic_id as varchar(20)) , 'Ambiguous!')
from posts p left outer join keywords k
on  p.content like '% ' + k.word + ' %'  -- whole word
    or p.content like k.word + ' %' --start with the word
    or p.content like '% ' + k.word -- end with the word
)
select 
post_id
, topic = string_agg(topic_id, ',') within group (order by topic_id)
from base
group by post_id
order by 1 
