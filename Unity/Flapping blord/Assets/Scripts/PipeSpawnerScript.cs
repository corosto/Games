using UnityEngine;

public class PipeSpawnerScript : MonoBehaviour {

    private float timer = 0;

    public GameObject pipe;
    public float spawnRate = 2;
    public float heightOffset = 8;

    void Start() {
        SpawnPipe();
    }

    void Update() {
        if (timer < spawnRate) {
            timer += Time.deltaTime;
        }
        else {
            SpawnPipe();
            timer = 0;
        }
    }

    void SpawnPipe() {
        Instantiate(pipe, new Vector3(transform.position.x, Random.Range(transform.position.y - heightOffset, transform.position.y + heightOffset), transform.position.z), transform.rotation);
    }
}
