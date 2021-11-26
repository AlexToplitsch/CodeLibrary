package json;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import json.objects.ValueObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class JSONReader {
    public ObjectMapper objectMapper;

    public JSONReader(){
        objectMapper = new ObjectMapper();
        configureObjectMapper();
    }

    private void configureObjectMapper() {
        objectMapper.configure(
                DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    }

    public static <T> T makeObjects (JsonNode node, Class<T> tClass) throws JsonProcessingException {
        return objectMapper.treeToValue(node, tClass);
    }
}
