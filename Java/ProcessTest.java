import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.*;


class ProcessTest {

    @Test
    void testCasoNormal() {
        List<String> input = Arrays.asList("abcdefghijkl", "short");
        Map<String, String> map = new HashMap<>();
        map.put("abcdefghijkl", "OK");
        map.put("short", "OK");

        List<String> result = new Main().process(input, map, "OK");

        assertEquals(1, result.size());
        assertEquals("abcdefghijkl", result.get(0));
    }

    @Test
    void testListaVacia() {
        List<String> result = new Main().process(new ArrayList<>(), new HashMap<>(), "OK");
        assertTrue(result.isEmpty());
    }

    @Test
    void testLongitudLimite() {
        List<String> input = Arrays.asList("1234567890"); // 10 chars
        Map<String, String> map = Map.of("1234567890", "OK");

        List<String> result = new Main().process(input, map, "OK");

        assertTrue(result.isEmpty());
    }

    @Test
    void testValorNoCoincide() {
        List<String> input = Arrays.asList("abcdefghijkl");
        Map<String, String> map = Map.of("abcdefghijkl", "NO");

        List<String> result = new Main().process(input, map, "OK");

        assertTrue(result.isEmpty());
    }

    @Test
    void testNullEnMapa() {
        List<String> input = Arrays.asList("abcdefghijkl");
        Map<String, String> map = new HashMap<>();

        assertThrows(NullPointerException.class, () -> {
            new Main().process(input, map, "OK");
        });
    }
}