using System;
using UnityEngine;

public class AudioManagerScript : MonoBehaviour
{
    public static AudioManagerScript AudioManagerInstance;

    public SoundScript[] musicSounds, sfxSounds;
    public AudioSource musicSource, sfxSource;

    private void Awake()
    {
        if (AudioManagerInstance == null)
        {
            AudioManagerInstance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void Start() {
        // PlayMusic("Music");
    }

    public void PlayMusic(string name)
    {
        SoundScript sound = Array.Find(musicSounds, x => x.name == name);

        if (sound != null)
        {
            musicSource.clip = sound.clip;
            musicSource.Play();
        }
    }

    public void PlaySFX(string name)
    {
        SoundScript sound = Array.Find(sfxSounds, x => x.name == name);

        if (sound != null)
        {
            sfxSource.clip = sound.clip;
            sfxSource.Play();
        }
    }
}
