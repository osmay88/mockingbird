# Examples of request matching in wiremock

This request matching code in java

```java
stubFor(any(urlPathEqualTo("/everything"))
  .withHeader("Accept", containing("xml"))
  .withCookie("session", matching(".*12345.*"))
  .withQueryParam("search_term", equalTo("WireMock"))
  .withBasicAuth("jeff@example.com", "jeffteenjefftyjeff")
  .withRequestBody(equalToXml("<search-results />"))
  .withRequestBody(matchingXPath("//search-results"))
  .withMultipartRequestBody(
  	aMultipart()
  		.withName("info")
  		.withHeader("Content-Type", containing("charset"))
  		.withBody(equalToJson("{}"))
  )
  .willReturn(aResponse()));
```

is translated to:
```json
{
  "request" : {
    "urlPath" : "/everything",
    "method" : "ANY",
    "headers" : {
      "Accept" : {
        "contains" : "xml"
      }
    },
    "queryParameters" : {
      "search_term" : {
        "equalTo" : "WireMock"
      }
    },
    "cookies" : {
      "session" : {
        "matches" : ".*12345.*"
      }
    },
    "bodyPatterns" : [ {
      "equalToXml" : "<search-results />"
    }, {
      "matchesXPath" : "//search-results"
    } ],
    "multipartPatterns" : [ {
      "matchingType" : "ANY",
      "headers" : {
        "Content-Disposition" : {
          "contains" : "name=\"info\""
        },
        "Content-Type" : {
          "contains" : "charset"
        }
      },
      "bodyPatterns" : [ {
        "equalToJson" : "{}"
      } ]
    } ],
    "basicAuthCredentials" : {
      "username" : "jeff@example.com",
      "password" : "jeffteenjefftyjeff"
    }
  },
  "response" : {
    "status" : 200
  }
}
```