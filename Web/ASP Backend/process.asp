<%
response.write("Enter a number between 1 and 5 in querystring!<br>")
response.write("Example: asp?num=1 or asp?num=2 or asp?num=3 or etc. <br><br>")


If request.cookies("time")<>"" Then
	response.write("Last Vist:" & request.cookies("time"))
	response.cookies("time")= Now()
Else
	response.write("This is your first visit!")
	response.cookies("time")= Now()
End If

num = Request.QueryString("num")
If num = 1 Then
	response.write("<style> body{ background-color: red; } </style>")	
ElseIf num = 2 Then
	response.write("<style> body{ background-color: blue; } </style>")
ElseIf num = 3 Then
	response.write("<style> body{ background-color: green; } </style>")
ElseIf num = 4 Then 
	response.write("<style> body{ background-color: yellow; } </style>")
Else 
	response.write("<style> body{ background-color: orange; } </style>")
End If

%>

