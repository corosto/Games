using UnityEngine;

public class PipeMovementScript : MonoBehaviour {

    public float moveSpeed = 5.0f;
    public float deadZone = -45.0f;

    void Update() {
        transform.position += Vector3.left * moveSpeed * Time.deltaTime;

        if (transform.position.x < deadZone) {
            Destroy(gameObject);
        }
    }
}
