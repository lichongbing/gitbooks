
```
curl -v -u 6a3feac16ff0fc98d1e146144a145350:api_token \
	-H "Content-Type: application/json" \
	-d '{"time_entry":{"description":"Meeting with possible clients","tags":["billed"],"duration":1200,"start":"2013-03-05T07:58:58.000Z","pid":123,"created_with":"curl"}}' \
	-X POST https://api.track.toggl.com/api/v8/time_entries

 ```
      

```
curl -v -u 6a3feac16ff0fc98d1e146144a145350:api_token \
-X GET https://api.track.toggl.com/api/v8/workspaces
```

```
[{
	"id": 4760695,
	"name": "873610008's workspace",
	"profile": 0,
	"premium": false,
	"admin": true,
	"default_hourly_rate": 0,
	"default_currency": "USD",
	"only_admins_may_create_projects": false,
	"only_admins_see_billable_rates": false,
	"only_admins_see_team_dashboard": false,
	"projects_billable_by_default": true,
	"rounding": 1,
	"rounding_minutes": 0,
	"api_token": "97b7ed9f13f8c2ce2226b605ad9e4521",
	"at": "2020-10-12T08:20:40+00:00",
	"ical_enabled": true
}]
```

```
curl -v -u 6a3feac16ff0fc98d1e146144a145350:api_token \
-X GET https://api.track.toggl.com/api/v8/workspaces/4760695/projects
```

```
[{
		"id": 164395689,
		"wid": 4760695,
		"name": "JS",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:43:57+00:00",
		"created_at": "2020-10-17T12:43:57+00:00",
		"color": "3",
		"auto_estimates": false,
		"hex_color": "#e36a00"
	}, {
		"id": 164326982,
		"wid": 4760695,
		"name": "上厕所",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-15T15:45:31+00:00",
		"created_at": "2020-10-15T15:45:31+00:00",
		"color": "3",
		"auto_estimates": false,
		"actual_hours": 1,
		"hex_color": "#e36a00"
	}, {
		"id": 164217727,
		"wid": 4760695,
		"name": "休息",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T08:27:38+00:00",
		"created_at": "2020-10-12T08:27:38+00:00",
		"color": "5",
		"auto_estimates": false,
		"actual_hours": 45,
		"hex_color": "#2da608"
	}, {
		"id": 164395439,
		"wid": 4760695,
		"name": "修车",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:02:39+00:00",
		"created_at": "2020-10-17T12:02:39+00:00",
		"color": "10",
		"auto_estimates": false,
		"actual_hours": 11,
		"hex_color": "#c7af14"
	}, {
		"id": 164395421,
		"wid": 4760695,
		"name": "做饭",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T11:59:33+00:00",
		"created_at": "2020-10-17T11:59:33+00:00",
		"color": "12",
		"auto_estimates": false,
		"hex_color": "#991102"
	}, {
		"id": 164395448,
		"wid": 4760695,
		"name": "公交",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:03:53+00:00",
		"created_at": "2020-10-17T12:03:53+00:00",
		"color": "1",
		"auto_estimates": false,
		"hex_color": "#9e5bd9"
	}, {
		"id": 164242509,
		"wid": 4760695,
		"name": "兼职",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-13T00:57:10+00:00",
		"created_at": "2020-10-13T00:57:10+00:00",
		"color": "10",
		"auto_estimates": false,
		"actual_hours": 10,
		"hex_color": "#c7af14"
	}, {
		"id": 164218751,
		"wid": 4760695,
		"name": "写博客",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T08:51:34+00:00",
		"created_at": "2020-10-12T08:51:34+00:00",
		"color": "3",
		"auto_estimates": false,
		"actual_hours": 22,
		"hex_color": "#e36a00"
	}, {
		"id": 164219541,
		"wid": 4760695,
		"name": "写算法",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T09:14:55+00:00",
		"created_at": "2020-10-12T09:14:55+00:00",
		"color": "12",
		"auto_estimates": false,
		"hex_color": "#991102"
	}, {
		"id": 164219674,
		"wid": 4760695,
		"name": "出门",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T09:17:20+00:00",
		"created_at": "2020-10-12T09:17:20+00:00",
		"color": "5",
		"auto_estimates": false,
		"actual_hours": 14,
		"hex_color": "#2da608"
	}, {
		"id": 164348102,
		"wid": 4760695,
		"name": "刷牙",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-16T01:07:52+00:00",
		"created_at": "2020-10-16T01:07:52+00:00",
		"color": "7",
		"auto_estimates": false,
		"hex_color": "#c9806b"
	}, {
		"id": 164395364,
		"wid": 4760695,
		"name": "加油",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T11:47:56+00:00",
		"created_at": "2020-10-17T11:47:56+00:00",
		"color": "10",
		"auto_estimates": false,
		"hex_color": "#c7af14"
	}, {
		"id": 164326830,
		"wid": 4760695,
		"name": "吃饭",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-15T15:39:12+00:00",
		"created_at": "2020-10-15T15:39:12+00:00",
		"color": "2",
		"auto_estimates": false,
		"actual_hours": 9,
		"hex_color": "#d94182"
	}, {
		"id": 164219766,
		"wid": 4760695,
		"name": "回家",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T09:20:18+00:00",
		"created_at": "2020-10-12T09:20:18+00:00",
		"color": "9",
		"auto_estimates": false,
		"actual_hours": 31,
		"hex_color": "#990099"
	}, {
		"id": 164395496,
		"wid": 4760695,
		"name": "图书馆",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:09:05+00:00",
		"created_at": "2020-10-17T12:09:05+00:00",
		"color": "10",
		"auto_estimates": false,
		"hex_color": "#c7af14"
	}, {
		"id": 164395435,
		"wid": 4760695,
		"name": "地铁",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:02:07+00:00",
		"created_at": "2020-10-17T12:02:07+00:00",
		"color": "9",
		"auto_estimates": false,
		"actual_hours": 5,
		"hex_color": "#990099"
	}, {
		"id": 164219419,
		"wid": 4760695,
		"name": "学习Java",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T09:11:22+00:00",
		"created_at": "2020-10-12T09:11:22+00:00",
		"color": "12",
		"auto_estimates": false,
		"actual_hours": 22,
		"hex_color": "#991102"
	}, {
		"id": 164219861,
		"wid": 4760695,
		"name": "家务",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T09:23:15+00:00",
		"created_at": "2020-10-12T09:23:15+00:00",
		"color": "3",
		"auto_estimates": false,
		"actual_hours": 11,
		"hex_color": "#e36a00"
	}, {
		"id": 164348072,
		"wid": 4760695,
		"name": "工作",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-16T01:06:34+00:00",
		"created_at": "2020-10-16T01:06:34+00:00",
		"color": "0",
		"auto_estimates": false,
		"actual_hours": 5,
		"hex_color": "#0b83d9"
	}, {
		"id": 164395483,
		"wid": 4760695,
		"name": "手机",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:07:55+00:00",
		"created_at": "2020-10-17T12:07:55+00:00",
		"color": "8",
		"auto_estimates": false,
		"actual_hours": 29,
		"hex_color": "#465bb3"
	}, {
		"id": 164348138,
		"wid": 4760695,
		"name": "早餐",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-16T01:10:59+00:00",
		"created_at": "2020-10-16T01:10:59+00:00",
		"color": "3",
		"auto_estimates": false,
		"actual_hours": 2,
		"hex_color": "#e36a00"
	}, {
		"id": 164395428,
		"wid": 4760695,
		"name": "洗头",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:00:53+00:00",
		"created_at": "2020-10-17T12:00:53+00:00",
		"color": "5",
		"auto_estimates": false,
		"hex_color": "#2da608"
	}, {
		"id": 164219804,
		"wid": 4760695,
		"name": "洗漱",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T09:21:22+00:00",
		"created_at": "2020-10-12T09:21:22+00:00",
		"color": "2",
		"auto_estimates": false,
		"actual_hours": 1,
		"hex_color": "#d94182"
	}, {
		"id": 164395426,
		"wid": 4760695,
		"name": "洗澡",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:00:31+00:00",
		"created_at": "2020-10-17T12:00:31+00:00",
		"color": "3",
		"auto_estimates": false,
		"hex_color": "#e36a00"
	}, {
		"id": 164395430,
		"wid": 4760695,
		"name": "洗脚",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:01:12+00:00",
		"created_at": "2020-10-17T12:01:12+00:00",
		"color": "13",
		"auto_estimates": false,
		"hex_color": "#d92b2b"
	}, {
		"id": 164325131,
		"wid": 4760695,
		"name": "洗脸",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-15T14:44:27+00:00",
		"created_at": "2020-10-15T14:44:27+00:00",
		"color": "14",
		"auto_estimates": false,
		"hex_color": "#525266"
	}, {
		"id": 164219781,
		"wid": 4760695,
		"name": "洗衣服",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T09:20:40+00:00",
		"created_at": "2020-10-12T09:20:40+00:00",
		"color": "9",
		"auto_estimates": false,
		"hex_color": "#990099"
	}, {
		"id": 164395442,
		"wid": 4760695,
		"name": "洗车",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:02:53+00:00",
		"created_at": "2020-10-17T12:02:53+00:00",
		"color": "0",
		"auto_estimates": false,
		"hex_color": "#0b83d9"
	}, {
		"id": 164325286,
		"wid": 4760695,
		"name": "理财",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-15T14:48:47+00:00",
		"created_at": "2020-10-15T14:48:47+00:00",
		"color": "13",
		"auto_estimates": false,
		"actual_hours": 3,
		"hex_color": "#d92b2b"
	}, {
		"id": 164395485,
		"wid": 4760695,
		"name": "电话",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:08:14+00:00",
		"created_at": "2020-10-17T12:08:14+00:00",
		"color": "9",
		"auto_estimates": false,
		"actual_hours": 18,
		"hex_color": "#990099"
	}, {
		"id": 164395477,
		"wid": 4760695,
		"name": "看书",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-17T12:07:08+00:00",
		"created_at": "2020-10-17T12:07:08+00:00",
		"color": "4",
		"auto_estimates": false,
		"hex_color": "#bf7000"
	}, {
		"id": 164218985,
		"wid": 4760695,
		"name": "睡觉",
		"billable": false,
		"is_private": true,
		"active": true,
		"template": false,
		"at": "2020-10-12T08:57:10+00:00",
		"created_at": "2020-10-12T08:57:10+00:00",
		"color": "7",
		"auto_estimates": false,
		"actual_hours": 87,
		"hex_color": "#c9806b"
	}, {
		"id": 164219900,
		"wid": 4760695,
		"name": "编* Connection #0 to host api.track.toggl.com left intact
		程 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 12 T09: 24: 15 + 00: 00 ","
		created_at ":"
		2020 - 10 - 12 T09: 24: 15 + 00: 00 ","
		color ":"
		10 ","
		auto_estimates ":false,"
		actual_hours ":9,"
		hex_color ":"#
		c7af14 "},{"
		id ":164395489,"
		wid ":4760695,"
		name ":"
		聊天 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 17 T12: 08: 28 + 00: 00 ","
		created_at ":"
		2020 - 10 - 17 T12: 08: 28 + 00: 00 ","
		color ":"
		4 ","
		auto_estimates ":false,"
		actual_hours ":55,"
		hex_color ":"#
		bf7000 "},{"
		id ":164395447,"
		wid ":4760695,"
		name ":"
		聚会 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 17 T12: 03: 37 + 00: 00 ","
		created_at ":"
		2020 - 10 - 17 T12: 03: 37 + 00: 00 ","
		color ":"
		4 ","
		auto_estimates ":false,"
		hex_color ":"#
		bf7000 "},{"
		id ":164242466,"
		wid ":4760695,"
		name ":"
		计划 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 13 T00: 52: 53 + 00: 00 ","
		created_at ":"
		2020 - 10 - 13 T00: 52: 53 + 00: 00 ","
		color ":"
		0 ","
		auto_estimates ":false,"
		actual_hours ":10,"
		hex_color ":"
		#0b83d9"},{"id":164223093,"wid":4760695,"name":"访友","billable":false,"is_private":true,"active":true,"template":false,"at":"2020-10-12T11:16:23+00:00","created_at":"2020-10-12T11:16:23+00:00","color":"12","auto_estimates":false,"actual_hours":14,"hex_color":"# 991102 "},{"
		id ":164219698,"
		wid ":4760695,"
		name ":"
		财务 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 12 T09: 18: 21 + 00: 00 ","
		created_at ":"
		2020 - 10 - 12 T09: 18: 21 + 00: 00 ","
		color ":"
		13 ","
		auto_estimates ":false,"
		hex_color ":"#
		d92b2b "},{"
		id ":164395492,"
		wid ":4760695,"
		name ":"
		购物 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 17 T12: 08: 50 + 00: 00 ","
		created_at ":"
		2020 - 10 - 17 T12: 08: 50 + 00: 00 ","
		color ":"
		8 ","
		auto_estimates ":false,"
		actual_hours ":3,"
		hex_color ":"
		#465bb3"},
        {"id":164326374,"wid":4760695,"name":"走路","billable":false,"is_private":true,"active":true,"template":false,"at":"2020-10-15T15:23:37+00:00","created_at":"2020-10-15T15:23:37+00:00","color":"5","auto_estimates":false,"actual_hours":8,"hex_color":"# 2 da608 "},{"
		id ":164217452,"
		wid ":4760695,"
		name ":"
		起床 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 12 T08: 24: 23 + 00: 00 ","
		created_at ":"
		2020 - 10 - 12 T08: 24: 23 + 00: 00 ","
		color ":"
		14 ","
		auto_estimates ":false,"
		actual_hours ":10,"
		hex_color ":"
		#525266"},{"id":164395443,"wid":4760695,"name":"跑步","billable":false,"is_private":true,"active":true,"template":false,"at":"2020-10-17T12:03:08+00:00","created_at":"2020-10-17T12:03:08+00:00","color":"8","auto_estimates":false,"hex_color":"# 465 bb3 "},{"
		id ":164326528,"
		wid ":4760695,"
		name ":"
		铲屎 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 15 T15: 29: 00 + 00: 00 ","
		created_at ":"
		2020 - 10 - 15 T15: 29: 00 + 00: 00 ","
		color ":"
		5 ","
		auto_estimates ":false,"
		actual_hours ":6,"
		hex_color ":"
		#2da608"},{"id":164395450,"wid":4760695,"name":"驾车","billable":false,"is_private":true,"active":true,"template":false,"at":"2020-10-17T12:04:07+00:00","created_at":"2020-10-17T12:04:07+00:00","color":"7","auto_estimates":false,"hex_color":"# c9806b "},{"
		id ":164219444,"
		wid ":4760695,"
		name ":"
		骑摩托车 ","
		billable ":false,"
		is_private ":true,"
		active ":true,"
		template ":false,"
		at ":"
		2020 - 10 - 12 T09: 12: 06 + 00: 00 ","
		created_at ":"
		2020 - 10 - 12 T09: 12: 06 + 00: 00 ","
		color ":"
		0 ","
		auto_estimates ":false,"
		actual_hours ":33,"
		hex_color ":"
		#0b83d9"},{"id":164395453,"wid":4760695,"name":"骑自行车","billable":false,"is_private":true,"active":true,"template":false,"at":"2020-10-17T12:04:28+00:00","created_at":"2020-10-17T12:04:28+00:00","color":"1","auto_estimates":false,"hex_color":"# 9e5 bd9 "}]
```
## 获取tags标签
```
curl -v -u 6a3feac16ff0fc98d1e146144a145350:api_token \
-X GET https://api.track.toggl.com/api/v8/workspaces/4760695/tags
```
## response
```
[{
	"id": 8732785,
	"wid": 4760695,
	"name": "billed",
	"at": "2020-11-02T01:59:38+00:00"
}, {
	"id": 8661246,
	"wid": 4760695,
	"name": "娱乐",
	"at": "2020-10-19T00:45:25+00:00"
}, {
	"id": 8661231,
	"wid": 4760695,
	"name": "财务",
	"at": "2020-10-19T00:38:26+00:00"
}, {
	"id": 8661230,
	"wid": 4760695,
	"name": "用餐",
	"at": "2020-10-19T00:37:39+00:00"
}, {
	"id": 8661201,
	"wid": 4760695,
	"name": "思考",
	"at": "2020-10-19T00:28:38+00:00"
}, {
	"id": 8661200,
	"wid": 4760695,
	"name": "工作",
	"at": "2020-10-19T00:28:26+00:00"
}, {
	"id": 8661191,
	"wid": 4760695,
	"name": "内务",
	"at": "2020-10-19T00:23:59+00:00"
}, {
	"id": 8661187,
	"wid": 4760695,
	"name": "运动",
	"at": "2020-10-19T00:23:24+00:00"
}, {
	"id": 8661186,
	"wid": 4760695,
	"name": "休息",
	"at": "2020-10-19T00:23:10+00:00"
}, {
	"id": 8661183,
	"wid": 4760695,
	"name": "社交",
	"at": "2020-10-19T00:23:01+00:00"
}, {
	"id": 8661180,
	"wid": 4760695,
	"name": "打理",
	"at": "2020-10-19T00:22:34+00:00"
}, {
	"id": 8661178,
	"wid": 4760695,
	"name": "学习",
	"at": "2020-10-19T00:21:29+00:00"
}, {
	"id": 8661177,
	"wid": 4760695,
	"name": "出行",
	"at": "2020-10-19T00:20:50+00:00"
}]

```

## 开始time_entries
```
curl -v -u 6a3feac16ff0fc98d1e146144a145350:api_token \
	-H "Content-Type: application/json" \
	-d '{"time_entry":{"description":"出门","tags":["出行"],"pid":164219444,"created_with":"curl"}}' \
	-X POST https://api.track.toggl.com/api/v8/time_entries/start
```
## response
```
{
	"data": {
		"id": 1752793442,
		"wid": 4760695,
		"pid": 164219444,
		"billable": false,
		"start": "2020-11-02T01:59:38Z",
		"duration": -1604282378,
		"description": "出门",
		"tags": ["billed"],
		"duronly": false,
		"at": "2020-11-02T01:59:38+00:00",
		"uid": 6226292
	}
}
```

```
curl -v -u 6a3feac16ff0fc98d1e146144a145350:api_token -H "Content-Type: application/json" -d '{"time_entry":{"description":"当前日期当前位置 (街道)","tags":["工作"],"pid":164242509,"created_with":"curl"}}' -X POST https://api.track.toggl.com/api/v8/time_entries/start

```