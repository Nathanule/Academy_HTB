from mitmproxy import ctx, http

class ModifyRequest:
	def request(self, flow: http.HTTPFlow) -> None:
	# Display the intercepted requested URL along with query parameters
            ctx.log.info("Incercepted Request URL:")
            ctx.log.info(flow.request.url)

            # display the inrecepted request parameters
            ctx.log.info("Intercepted Request Paramerters:")
            for key, value in flow.request.query.items():
                ctx.log.info(f'{key}: {value}')

        #Modify the parameters if needed
            flow.request.query["param_name"] = "new_value"

        #Modify the request body if needed
            flow.request.text = "new_request_body"

addons = [
    ModifyRequest
]
