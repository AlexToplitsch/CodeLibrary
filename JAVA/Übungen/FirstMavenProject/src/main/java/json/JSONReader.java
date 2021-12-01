package json;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;

public class JSONReader {
    // ##### Properties #####
    public ObjectMapper objectMapper;


    // ##### Constructor #####
    public JSONReader() {
        objectMapper = new ObjectMapper();
        configureObjectMapper();
    }


    // ##### Functions #####

    /**
     * Configures the ObjectMapper to not fail on unknown properties
     */
    private void configureObjectMapper() {
        objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    }

    /**
     *  Tries to create an object from a JSON file that takes places in the abstract  path
     *  "src" and returns an object that is passed in tClass
     * @param src The abstract path where the file is saved
     * @param tClass The class type from which an instance should be created
     * @param <T> Class type that is passed in tClass
     * @return An instance of the passed class type in tClass
     * @throws IOException If parsing was not successful or the file was not found
     * @throws UnsupportedOperationException If the file could not be created
     */
    public <T> T makeObjects(String src, Class<T> tClass) throws IOException, UnsupportedOperationException {
        File f = Paths.get(src)
                      .toFile();
        return objectMapper.readValue(f, tClass);
    }

    public JsonNode objectToJson(Object o){
        return objectMapper.valueToTree(o);
    }
}
