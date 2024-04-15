"""

Reverse-engineered authentication keys for the GeoCache.com API

"""

auth_keys_jwt = ["eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoia29qaXVneXZnaCIsInBnZCI6IjJkMDNjMGQ0LWZjOWEtNGMzYS1hZDY1LTg3MTVjNTE1ZTZiZCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNDkwOTY0OTQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiUHVibGljIiwiQmFzaWMiXSwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy91c2VyZGF0YSI6IjFFOUMwNEY3LTYzMEItNDZGMy04NUM1LUVFMDhDMDk4NkQ2NiIsImxnZCI6IjM2YTcwNjQ5LWQ5ZTktNDM3OS05ZjYxLWNjMDBlOTIwNWU5NCIsInNjb3BlIjpbIndlYiIsIm1hcHRpbGUiLCJnYXJtaW4iXSwibmJmIjoxNzEyNTE1OTcxLCJleHAiOjE3MTI1MTk1NzEsImlzcyI6Imh0dHBzOi8vb2F1dGguZ2VvY2FjaGluZy5jb20vdG9rZW4iLCJhdWQiOiIxZTljMDRmNy02MzBiLTQ2ZjMtODVjNS1lZTA4YzA5ODZkNjYifQ.31os6tpKnJ5_oSjPcZ2ZLMUsu7xqmBhnfHn_BVzf8Ec",
                 "eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiMGk5dW84Z3lmdGdodmpia25sbSIsInBnZCI6IjMyMGUyYzIyLTZhODItNDIyMC05ZjMzLTVmZGVjNWZhOTQ5OSIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNDkxMTg2NjYiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiUHVibGljIiwiQmFzaWMiXSwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy91c2VyZGF0YSI6IjFFOUMwNEY3LTYzMEItNDZGMy04NUM1LUVFMDhDMDk4NkQ2NiIsImxnZCI6IjM2YTcwNjQ5LWQ5ZTktNDM3OS05ZjYxLWNjMDBlOTIwNWU5NCIsInNjb3BlIjpbIndlYiIsIm1hcHRpbGUiLCJnYXJtaW4iXSwibmJmIjoxNzEyNTE2MDk2LCJleHAiOjE3MTI1MTk2OTYsImlzcyI6Imh0dHBzOi8vb2F1dGguZ2VvY2FjaGluZy5jb20vdG9rZW4iLCJhdWQiOiIxZTljMDRmNy02MzBiLTQ2ZjMtODVjNS1lZTA4YzA5ODZkNjYifQ.CZ2oMi_57GnsHNAVVmmiTqRwSjKQcgBUTqsMSfHhqPQ",
                 #"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiamhndmdoamdoZnl0NzY1NCIsInBnZCI6IjQ3ZjU5NGU2LTkxMTAtNDU0Zi04NGIzLWJjNzI0ZWEwMmI4NyIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNDkxMTg2ODIiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiUHVibGljIiwiQmFzaWMiXSwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy91c2VyZGF0YSI6IjFFOUMwNEY3LTYzMEItNDZGMy04NUM1LUVFMDhDMDk4NkQ2NiIsImxnZCI6IjM2YTcwNjQ5LWQ5ZTktNDM3OS05ZjYxLWNjMDBlOTIwNWU5NCIsInNjb3BlIjpbIndlYiIsIm1hcHRpbGUiLCJnYXJtaW4iXSwibmJmIjoxNzEyNTE2MjE1LCJleHAiOjE3MTI1MTk4MTUsImlzcyI6Imh0dHBzOi8vb2F1dGguZ2VvY2FjaGluZy5jb20vdG9rZW4iLCJhdWQiOiIxZTljMDRmNy02MzBiLTQ2ZjMtODVjNS1lZTA4YzA5ODZkNjYifQ.ob70BfYmh0X8-Cos9Zbo8lnNS-FcagH2mXgbw-zaYOU",
                 "eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYWVnaHRxcmVRRVdHUiIsInBnZCI6ImJiMTUyNTI5LTBiMjUtNDhjMS04ZjU5LTU3MzllNmMzYjU3YiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNDkxMTg4MDUiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiUHVibGljIiwiQmFzaWMiXSwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy91c2VyZGF0YSI6IjFFOUMwNEY3LTYzMEItNDZGMy04NUM1LUVFMDhDMDk4NkQ2NiIsImxnZCI6IjM2YTcwNjQ5LWQ5ZTktNDM3OS05ZjYxLWNjMDBlOTIwNWU5NCIsInNjb3BlIjpbIndlYiIsIm1hcHRpbGUiLCJnYXJtaW4iXSwibmJmIjoxNzEyNTE2NjAyLCJleHAiOjE3MTI1MjAyMDIsImlzcyI6Imh0dHBzOi8vb2F1dGguZ2VvY2FjaGluZy5jb20vdG9rZW4iLCJhdWQiOiIxZTljMDRmNy02MzBiLTQ2ZjMtODVjNS1lZTA4YzA5ODZkNjYifQ.AhDDtQRBOfxnQkBGyAUkWwFztnUIovUnMtKvY7-eo4E"]

auth_keys_gspk = ["YDbwZXLJc_9IfOjaJlmc6AyOS-AQ-fvyXZfgM9e1GfmknVReOC9Jr9x80Ji7Glh6fNqSPB8O7feFotOUnQNhEM60Bysmh94etw4PLbxDI3rjiTsLuyN7g8uKDtr_Ux21tG8wOuoqV0EeJfFkP6tpAiKrhMBHbpNPi0xZO8jT_7c1",
                  "CH8zvTTMwI6b_sy6cBAMEP3V25N_lU3U19qWjm59b614oaT6AipQsbfl4t_9aiY-4WBl-N5EhiVu49TdIhwkpRxbxh_m8Ew2SPa4kIbv3smIHvXs9OsN5PtIiZNb7OhhR4fRtEAS69WUnKLtUSPETkqFy1GBoiIvNGzmngQHz6Q1",
                  #"",
                  "wRHqWtLZ5GJyBjEN0nChG63BiOykGQnAaX4epuuUoa7BaTUjp6o4BtK5yBdJv3nqups56We6cEt8cBKrwOnkDUy6DRmX6hsePLvi6tE4rtMGjMMgrmx8PmhSS8Cesqg_EfchigI28CKE-7Fg3qn63qunZG8ifpeBHYjNc-rJ9OE1"]


"""

#auth = HTTPBasicAuth("quebueno", "testing123")


#cookies = {'ASP.NET_SessionId': '3oh2qutk4hm5o4s2ofhizohb','CookieConsent':'{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:3%2Cutc:1712177688863%2Cregion:%27CA%27}','Culture':'en-US','__RequestVerificationToken':'AdHZ16l6r56c2hLxmIYeshZ65JBwE5w8aS0-VahwkBVENJDanDk-CjVkkLAVG2vGfnOGTAbNSOoBasBFvFhwFi0Ke9Y1','_csrf':'PMXXDNgWBPmPDdUOcRUwZ5pH','ai_user':"kTyxnaLuB23EG5Fqmxar+C|2024-04-03T20:55:12.361Z","gpt_ppid50":"nBvbWwhASDOWmn6G699xLkGD5Thv3BrlTZqPbJClBL6P10dpCI","gspkauth":"a3tOVV1OFJo_byrZ2ymbkDAkBhG0_AuJ0cZ0ikqzl1JdkX8d5aEgq63iGaR44wTQ3vROVGh53_gcDLSFv58V9FZCOwLGn_2JKvaZuf8MlaEJCQepouzEOlqkwt9T4nvNN-vw9psSBGdYDj2E9_NC8eg8fwWqfYrsB0daQ-yVh5E1","jwt":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoicXVlYnVlbm8iLCJwZ2QiOiIzNmUwNjZjZC05OGMyLTRlYjQtOGZmNy1jZjliM2VmY2UwMjUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ5MDkwNTEyIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjpbIlB1YmxpYyIsIkJhc2ljIl0sImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdXNlcmRhdGEiOiIxRTlDMDRGNy02MzBCLTQ2RjMtODVDNS1FRTA4QzA5ODZENjYiLCJsZ2QiOiIzNmE3MDY0OS1kOWU5LTQzNzktOWY2MS1jYzAwZTkyMDVlOTQiLCJzY29wZSI6WyJ3ZWIiLCJtYXB0aWxlIiwiZ2FybWluIl0sIm5iZiI6MTcxMjM2ODMzMCwiZXhwIjoxNzEyMzcxOTMwLCJpc3MiOiJodHRwczovL29hdXRoLmdlb2NhY2hpbmcuY29tL3Rva2VuIiwiYXVkIjoiMWU5YzA0ZjctNjMwYi00NmYzLTg1YzUtZWUwOGMwOTg2ZDY2In0.BJsIjo0cSoR57p2Rq44BpZ5g0JRtXcsWa_eFQ1GlmL0"}
#cookies = {'CookieConsent':'{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:3%2Cutc:1712177688863%2Cregion:%27CA%27}','_csrf':'PMXXDNgWBPmPDdUOcRUwZ5pH','ai_user':'kTyxnaLuB23EG5Fqmxar+C|2024-04-03T20:55:12.361Z','gpt_ppid50':'nBvbWwhASDOWmn6G699xLkGD5Thv3BrlTZqPbJClBL6P10dpCI'}

#cookies = {"jwt":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYXl5eXkxMjM0NSIsInBnZCI6IjI0ZDNiYmVmLTcwOGItNGMxOS1hMmEyLTQ5N2RiOGM5N2M0NiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNDkwOTUyNzAiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiUHVibGljIiwiQmFzaWMiXSwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy91c2VyZGF0YSI6IjFFOUMwNEY3LTYzMEItNDZGMy04NUM1LUVFMDhDMDk4NkQ2NiIsImxnZCI6IjM2YTcwNjQ5LWQ5ZTktNDM3OS05ZjYxLWNjMDBlOTIwNWU5NCIsInNjb3BlIjpbIndlYiIsIm1hcHRpbGUiLCJnYXJtaW4iXSwibmJmIjoxNzEyNDA5MjgyLCJleHAiOjE3MTI0MTI4ODIsImlzcyI6Imh0dHBzOi8vb2F1dGguZ2VvY2FjaGluZy5jb20vdG9rZW4iLCJhdWQiOiIxZTljMDRmNy02MzBiLTQ2ZjMtODVjNS1lZTA4YzA5ODZkNjYifQ._3KotFlMuUi9LhnXKnyg6VqqQU2XWfpkCnsJT_fGY5s"}

#cookies = {"gspkauth":"a3tOVV1OFJo_byrZ2ymbkDAkBhG0_AuJ0cZ0ikqzl1JdkX8d5aEgq63iGaR44wTQ3vROVGh53_gcDLSFv58V9FZCOwLGn_2JKvaZuf8MlaEJCQepouzEOlqkwt9T4nvNN-vw9psSBGdYDj2E9_NC8eg8fwWqfYrsB0daQ-yVh5E1","jwt":"eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoicXVlYnVlbm8iLCJwZ2QiOiIzNmUwNjZjZC05OGMyLTRlYjQtOGZmNy1jZjliM2VmY2UwMjUiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjQ5MDkwNTEyIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjpbIlB1YmxpYyIsIkJhc2ljIl0sImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdXNlcmRhdGEiOiIxRTlDMDRGNy02MzBCLTQ2RjMtODVDNS1FRTA4QzA5ODZENjYiLCJsZ2QiOiIzNmE3MDY0OS1kOWU5LTQzNzktOWY2MS1jYzAwZTkyMDVlOTQiLCJzY29wZSI6WyJ3ZWIiLCJtYXB0aWxlIiwiZ2FybWluIl0sIm5iZiI6MTcxMjM2ODMzMCwiZXhwIjoxNzEyMzcxOTMwLCJpc3MiOiJodHRwczovL29hdXRoLmdlb2NhY2hpbmcuY29tL3Rva2VuIiwiYXVkIjoiMWU5YzA0ZjctNjMwYi00NmYzLTg1YzUtZWUwOGMwOTg2ZDY2In0.BJsIjo0cSoR57p2Rq44BpZ5g0JRtXcsWa_eFQ1GlmL0"}

"""
