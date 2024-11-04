using UnityEngine;

public class BirdScript : MonoBehaviour
{

  private LogicScript logicScript;

  public Rigidbody2D myRigidbody;
  public Animator myAnimator;
  public float flapStrength = 8.0f;
  public bool birdAlive = true;

  private void Start()
  {
    logicScript = GameObject.FindGameObjectWithTag("Logic").GetComponent<LogicScript>();
  }

  void Update()
  {
    if (Input.GetKeyDown(KeyCode.Space) && birdAlive)
    {
      myRigidbody.linearVelocity = Vector2.up * flapStrength;

      myAnimator.Play("Wings_Flap");

      AudioManagerScript.AudioManagerInstance.PlaySFX("Wing");
    }

    if (myRigidbody.position.y < -17)
    {
      death();
    }
  }

  private void OnCollisionEnter2D(Collision2D collision)
  {
    AudioManagerScript.AudioManagerInstance.PlaySFX("Hit");
    death();
  }

  private void death()
  {
    birdAlive = false;
    AudioManagerScript.AudioManagerInstance.PlaySFX("Die");
    logicScript.gameOver();
  }
}

