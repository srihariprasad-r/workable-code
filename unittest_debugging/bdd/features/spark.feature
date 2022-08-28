Feature: Some basic PySpark examples

  Scenario: Simple join of two tables
    Given a spark session
    And a table called "students" containing
      | id:Int   | name:String      | sid:String   | score:Int  |      
      | 1        | Fred             | 1            | 100        |         
      | 2        | Sally            | 1            | 98         |     
      | 3        | Susan            | 1            | 96         |     
      | 4        | Mark             | 1            | 59         |     
      | 5        | Fred             | 2            | 33         |     
      | 6        | Sally            | 2            | 22         |     
      | 7        | Susan            | 2            | 75         |     
      | 8        | Mark             | 2            | 0          |      
      | 9        | Fred             | 3            | 100        |        
      | 10       | Sally            | 3            | 28         |     
      | 11       | Susan            | 3            | 89         |     
      | 12       | Mark             | 3            | 40         |     
    And a table called "subjects" containing
      | id:Int | name:String |
      | 1      | Maths       |
      | 2      | Physics     |
      | 3      | Chemistry   |
    When I do the join business logic
    Then the table "results" contains
      | id:Int | student_name:String | subject_name:String |
      | 1      | Fred                | Maths               |
      | 2      | Sally               | Maths               |
      | 3      | Susan               | Maths               |
      | 4      | Mark                | Maths               |
      | 5      | Fred                | Physics             |
      | 6      | Sally               | Physics             |
      | 7      | Susan               | Physics             |
      | 8      | Mark                | Physics             |
      | 9      | Fred                | Chemistry           |
      | 10     | Sally               | Chemistry           |
      | 11     | Susan               | Chemistry           |
      | 12     | Mark                | Chemistry           |
    When I find maximum score in "students"
    Then the table "max_results" shows maximum score rows
      | id:Int   | name:String      | sid:String   | score:Int  |      
      | 1        | Fred             | 1            | 100        | 
      | 9        | Fred             | 3            | 100        |        
