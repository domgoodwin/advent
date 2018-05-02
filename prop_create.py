# //		[DirectDom("Url")]
# 		[ReadOnlyProperty]		
# 		public string Url { get { return this._Url.TypedValue; } private set { this._Url.TypedValue = value;} }
# 		protected PropertyHolder<string> _Url = new PropertyHolder<string>("Url");

import pyperclip




output  = ""

names = ["ContentType","StatusCode","ResponseBody","RequestBody","ErrorMessage","Success","ServerUsername","ServerPassword","WinAuthForServer","ProxyUrl","ProxyPort","ProxyDomain","ProxyUsername","ProxyPassword","WinAuthForProxy"]


# for name in names:
#     line = """[DirectDom("{0}")]
#             [ReadOnlyProperty]		
#             public string {0} {{ get {{ return this._{0}.TypedValue; }} private set {{ this._{0}.TypedValue = value;}} }}
#             protected PropertyHolder<string> _{0} = new PropertyHolder<string>("{0}");"""
#     line = line.format(name)
#     output += line + "\n"

for name in names:
    line = "this._{0}.TypedValue = string.Empty;"
    line = line.format(name)
    output += line + "\n"

pyperclip.copy(output)
print(output)