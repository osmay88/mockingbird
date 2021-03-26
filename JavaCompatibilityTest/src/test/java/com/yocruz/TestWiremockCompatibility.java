package com.yocruz;
import com.github.tomakehurst.wiremock.client.WireMock;
import org.junit.Test;


import static com.github.tomakehurst.wiremock.client.WireMock.stubFor;
import static com.github.tomakehurst.wiremock.client.WireMock.get;
import static com.github.tomakehurst.wiremock.client.WireMock.equalTo;
import static com.github.tomakehurst.wiremock.client.WireMock.urlEqualTo;
import static com.github.tomakehurst.wiremock.client.WireMock.aResponse;

public class TestWiremockCompatibility {

    public TestWiremockCompatibility() {
        WireMock.configureFor("localhost", 5000);
    }


    @Test
    public void endpointsCanBeCreated() {

        stubFor(get(urlEqualTo("/my/resource"))
                .withHeader("Accept", equalTo("text/xml"))
                .willReturn(aResponse()
                        .withStatus(200)
                        .withHeader("Content-Type", "text/xml")
                        .withBody("<response>Some content</response>")));

    }
}
