BOOKING_SCHEMA = {
"type": "object",
    "properties": {
        "bookingid": {
            "type": "integer"
        },
        "booking": {
            "type": "object",
                "properties": {
                    "firstname": {
                        "type": "string"
                    },
                    "lastname": {
                        "type": "string"
                    },
                    "totalprice": {
                        "type": "integer"
                    },
                    "depositpaid": {
                        "type": "boolean"
                    },
                    "bookingdates": {
                        "type": "object",
                            "properties": {
                                "checkin": {
                                    "type": "date"
                                },
                                "checkout": {
                                    "type": "date"
                                }
                            }
                    }
                },
            "additionalProperties": False
        },
    }
}

