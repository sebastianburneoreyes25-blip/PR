import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public public class Processor {

    public List<String> filterValidStrings(List<String> inputList, Map<String, String> valueMap, String expectedValue) {

        List<String> result = new ArrayList<>();

        for (String element : inputList) {
            if (isValid(element, valueMap, expectedValue)) {
                result.add(element);
            }
        }

        return result;
    }

    private boolean isValid(String element,
                            Map<String, String> valueMap,
                            String expectedValue) {

        if (element == null || valueMap == null) {
            return false;
        }

        String value = valueMap.get(element);

        return value != null &&
               value.equals(expectedValue) &&
               element.length() > 10;
    }
}

