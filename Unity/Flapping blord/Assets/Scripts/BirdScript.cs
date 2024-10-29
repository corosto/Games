using UnityEngine;

public class BirdScript : MonoBehaviour {

    private LogicScript logicScript;

    public Rigidbody2D myRigidbody;
    public float flapStrength = 8.0f;
    public bool birdAlive = true;

    private void Start() {
        logicScript = GameObject.FindGameObjectWithTag("Logic").GetComponent<LogicScript>();
    }

    void Update() {
        if (Input.GetKeyDown(KeyCode.Space) && birdAlive) {
            myRigidbody.linearVelocity = Vector2.up * flapStrength;
        }
    }

    private void OnCollisionEnter2D(Collision2D collision) {
        logicScript.gameOver();
        birdAlive = false;
    }
}

