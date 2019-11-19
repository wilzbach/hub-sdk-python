class OutputUtils:
    @staticmethod
    def parse_type(data):
        """
        Convert a OMS `data` JSON file into an Output type.
        """

        ty = data["type"]

        if ty == "list":
            from storyhub.sdk.service.output.OutputList import OutputList

            return OutputList.from_dict(data)
        if ty == "map":
            from storyhub.sdk.service.output.OutputMap import OutputMap

            return OutputMap.from_dict(data)
        if ty == "object":
            from storyhub.sdk.service.output.OutputObject import OutputObject

            return OutputObject.from_dict(data)
        if ty == "int" or ty == "number":
            from storyhub.sdk.service.output.OutputInt import OutputInt

            return OutputInt.from_dict(data)
        if ty == "float":
            from storyhub.sdk.service.output.OutputFloat import OutputFloat

            return OutputFloat.from_dict(data)
        if ty == "boolean":
            from storyhub.sdk.service.output.OutputBoolean import OutputBoolean

            return OutputBoolean.from_dict(data)
        if ty == "enum":
            from storyhub.sdk.service.output.OutputEnum import OutputEnum

            return OutputEnum.from_dict(data)
        if ty == "regex":
            from storyhub.sdk.service.output.OutputRegex import OutputRegex

            return OutputRegex.from_dict(data)
        if ty == "none":
            from storyhub.sdk.service.output.OutputNone import OutputNone

            return OutputNone.from_dict(data)
        if ty == "any":
            from storyhub.sdk.service.output.OutputAny import OutputAny

            return OutputAny.from_dict(data)

        from storyhub.sdk.service.output.OutputString import OutputString

        assert ty == "string", f"{ty} with {data} is unknown"
        return OutputString.from_dict(data)
