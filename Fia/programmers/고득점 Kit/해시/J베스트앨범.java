import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Solution {

    public List<Integer> solution(String[] genres, int[] plays) {
        HashMap<String, ArrayList> songsByGenres = new HashMap<>();
        HashMap<String, Integer> totalPlays = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            totalPlays.put(genres[i], totalPlays.getOrDefault(genres[i], 0) + plays[i]);
            songsByGenres.computeIfAbsent(genres[i], k -> new ArrayList<>()).add(List.of(i, plays[i]));
        }

        List<Map.Entry<String, Integer>> orderedPlays = new ArrayList<>(totalPlays.entrySet());
        Collections.sort(orderedPlays, Comparator.comparing(Map.Entry::getValue, Comparator.reverseOrder()));

        List<Integer> bestAlbum = new ArrayList<>();

        for (Map.Entry<String, Integer> play : orderedPlays) {
            List<List<Integer>> orderedSongs = new ArrayList<>(songsByGenres.get(play.getKey()));
            Collections.sort(orderedSongs, Comparator.comparing((List<Integer> song) -> song.get(1), Comparator.reverseOrder()).thenComparing(song -> song.get(0)));

            for (int i = 0; i < 2; i++) {
                if (orderedSongs.size() > i) {
                    bestAlbum.add(orderedSongs.get(i).get(0));
                }
            }
        }

        return bestAlbum;
    }

}
