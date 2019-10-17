from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    """
    Encode float x between -1 and 1 as two bytes.
    """
    i = int( 16380 * x )
    return Struct('h').pack(i)

def play( sampler, name = 'song.wav', seconds = 2 ):
    """
    Write the output of a sampler function as a wav file.
    """
    out = open( name, 'wb' )
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes( encode( sample ) )
        t = t +  1
    out.close()

def tri( frequency, amplitude = 0.3 ):
    """
    A continous triangle wave.
    """
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor( t / period + 0.5 )
        tri_wave = 2 * abs( 2 * saw_wave ) - 1
        return amplitude + tri_wave
    return sampler 

c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

def both(f,g):
    return lambda t: f(t) + g(t)

def triple( f,g,h ):
    return lambda t: f(t) + g(t) + h(t)

def note( f, start, end, fade = 0.01 ):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return ( seconds - start ) / fade * f(t)
        elif seconds > end - fade :
            return ( end - seconds ) / fade * f(t)
        else:
            return f(t)
    return sampler

def c_harmony():
    a = tri(c_freq)
    b = tri(e_freq)
    c = tri(g_freq)
    d = triple( tri(c_freq), tri(e_freq), tri(g_freq))
    play(a)
    play(b)
    play(c)
    play(d)

#play( both( tri(c_freq), tri(e_freq) ) )
#play( triple( tri(c_freq), tri(e_freq), tri(g_freq)) )
#play( note( c, 0, 1 / 4 ) )
c, e = tri(c_freq), tri(e_freq)
g, low_g = tri( g_freq ), tri(g_freq/2)
#play( both( note( c,0,1/4 ), note( e,1/2,1 ) ) )

z = 0
song = note( e, z, z + 1/8 )
z += 1/8
song = both(song,note( e, z, z + 1/8 ))
z += 1/4
song = both(song,note( c, z, z + 1/8 ))
z += 1/4
song = both(song,note( e, z, z + 1/8 ))
z += 1/8
song = both(song,note( e, z, z + 1/8 ))
z += 1/4
song = both(song,note( g, z, z + 1/4 ))
z += 1/2
song = both(song,note( low_g, z, z + 1/4 ))
z += 1/2
play(song)
