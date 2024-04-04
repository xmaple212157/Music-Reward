from utils import *
import os
import pickle
from musthe import *
import numpy as np

path_train_data = os.path.join(os.getcwd(), 'train_data_linear.npz')
path_dictionary = os.path.join(os.getcwd(), 'dictionary.pkl')

dictionary = pickle.load(open(path_dictionary, 'rb'))
event2word, word2event = dictionary
train_data = np.load(path_train_data)


def example_1():
    cnt_bar = 1
    for i in range(50):
        word = train_data['x'][0][i]
        print('bar:', cnt_bar, end='  | ')
        print_word_cp(word2event, word)
        if word2event['bar-beat'][word[2]] == 'Bar':
            cnt_bar += 1

    write_midi(train_data['x'][0][:50], 'test1.mid', word2event)


def example_2():
    words = []

    # position beat_0
    words.append([
        event2word['tempo']['Tempo_131'], event2word['chord']['CONTI'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])

    # C4 eigth note
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C4").number}'],
        event2word['duration']['Note_Duration_240'],
        event2word['velocity']['Note_Velocity_60']
    ])

    # E4 quater note
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("E4").number}'],
        event2word['duration']['Note_Duration_480'],
        event2word['velocity']['Note_Velocity_60']
    ])

    # position beat_1
    words.append([
        event2word['tempo']['CONTI'], event2word['chord']['CONTI'],
        event2word['bar-beat']['Beat_1'], event2word['type']['Metrical'], 0, 0,
        0
    ])
    # G4 eigth note
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("G4").number}'],
        event2word['duration']['Note_Duration_240'],
        event2word['velocity']['Note_Velocity_60']
    ])

    # new bar
    words.append([
        0, 0, event2word['bar-beat']['Bar'], event2word['type']['Metrical'], 0,
        0, 0
    ])

    # position beat_0
    words.append([
        event2word['tempo']['CONTI'], event2word['chord']['CONTI'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])
    # B5 whole note
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("B5").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    write_midi(words, 'test2.mid', word2event)


def example_3():
    # asume that the key is C major
    reward = 0
    for i in range(50):
        word = train_data['x'][0][i]
        vals = []
        for kidx, key in enumerate(word2event.keys()):
            vals.append(word2event[key][word[kidx]])

        if vals[3] == 'Note':
            pitch_number = int(vals[4].split('_')[-1])
            pitch = number_to_note(pitch_number)
            if '#' in pitch:
                reward -= 1
    print(reward)


def example_4():
    # functional chord
    T = ['C_M', 'E_m']
    D = ['G_M', 'B_o']
    SD = ['F_M', 'D_m', 'A_m']

    words = []
    words.append([
        event2word['tempo']['Tempo_131'], event2word['chord']['C_M'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("E4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("G4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, event2word['bar-beat']['Bar'], event2word['type']['Metrical'], 0,
        0, 0
    ])
    words.append([
        event2word['tempo']['CONTI'], event2word['chord']['F_M'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("F4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("A4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C5").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, event2word['bar-beat']['Bar'], event2word['type']['Metrical'], 0,
        0, 0
    ])
    words.append([
        event2word['tempo']['CONTI'], event2word['chord']['G_M'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("G4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("B4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("D5").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, event2word['bar-beat']['Bar'], event2word['type']['Metrical'], 0,
        0, 0
    ])
    words.append([
        event2word['tempo']['Tempo_131'], event2word['chord']['C_M'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("E4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("G4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, event2word['bar-beat']['Bar'], event2word['type']['Metrical'], 0,
        0, 0
    ])
    words.append([
        event2word['tempo']['CONTI'], event2word['chord']['G_M'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("G4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("B4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("D5").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, event2word['bar-beat']['Bar'], event2word['type']['Metrical'], 0,
        0, 0
    ])
    words.append([
        event2word['tempo']['CONTI'], event2word['chord']['F_M'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("F4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("A4").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])
    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C5").number}'],
        event2word['duration']['Note_Duration_1920'],
        event2word['velocity']['Note_Velocity_60']
    ])

    reward = 0
    last_chord = None
    for word in words:
        vals = []
        for kidx, key in enumerate(word2event.keys()):
            vals.append(word2event[key][word[kidx]])

        if vals[3] == 'Metrical' and vals[1] != 'CONTI' and vals[1] != 0:
            if last_chord is not None:
                if vals[1] in SD and last_chord in D:
                    reward -= 1
            last_chord = vals[1]

    print(reward)


def example_5():
    words = []

    words.append([
        event2word['tempo']['Tempo_131'], event2word['chord']['CONTI'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])

    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C4").number}'],
        event2word['duration']['Note_Duration_240'],
        event2word['velocity']['Note_Velocity_60']
    ])

    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("E4").number}'],
        event2word['duration']['Note_Duration_480'],
        event2word['velocity']['Note_Velocity_60']
    ])

    words.append([
        event2word['tempo']['Tempo_131'], event2word['chord']['CONTI'],
        event2word['bar-beat']['Beat_1'], event2word['type']['Metrical'], 0, 0,
        0
    ])

    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("F7").number}'],
        event2word['duration']['Note_Duration_480'],
        event2word['velocity']['Note_Velocity_60']
    ])

    def interval_reward(src_idx, dst_idx, words):
        src_notes = []
        for i in range(src_idx + 1, len(words)):
            vals = []
            for kidx, key in enumerate(word2event.keys()):
                vals.append(word2event[key][words[i][kidx]])

            if vals[3] == 'Note':
                src_notes.append(int(vals[4].split('_')[-1]))
            else:
                break

        dst_notes = []
        for i in range(dst_idx + 1, len(words)):
            vals = []
            for kidx, key in enumerate(word2event.keys()):
                vals.append(word2event[key][words[i][kidx]])

            if vals[3] == 'Note':
                dst_notes.append(int(vals[4].split('_')[-1]))
            else:
                break

        if max(dst_notes) > max(src_notes):
            if (Note(number_to_note(max(dst_notes))) -
                    Note(number_to_note(max(src_notes)))).number > 8:
                return -1

        return 0

    print(interval_reward(0, 3, words))

def example_6():
    words = []

    words.append([
        event2word['tempo']['Tempo_131'], event2word['chord']['CONTI'],
        event2word['bar-beat']['Beat_0'], event2word['type']['Metrical'], 0, 0,
        0
    ])

    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C4").number}'],
        event2word['duration']['Note_Duration_240'],
        event2word['velocity']['Note_Velocity_60']
    ])

    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("E4").number}'],
        event2word['duration']['Note_Duration_480'],
        event2word['velocity']['Note_Velocity_60']
    ])

    words.append([
        event2word['tempo']['Tempo_131'], event2word['chord']['CONTI'],
        event2word['bar-beat']['Beat_1'], event2word['type']['Metrical'], 0, 0,
        0
    ])

    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C4").number}'],
        event2word['duration']['Note_Duration_480'],
        event2word['velocity']['Note_Velocity_60']
    ])

    words.append([
        0, 0, 0, event2word['type']['Note'],
        event2word['pitch'][f'Note_Pitch_{Note("C5").number}'],
        event2word['duration']['Note_Duration_480'],
        event2word['velocity']['Note_Velocity_60']
    ])

    def repeat_note(src_idx, dst_idx, words):
        repeat_number = 0
        src_notes = []
        for i in range(src_idx + 1, len(words)):
            vals = []
            for kidx, key in enumerate(word2event.keys()):
                vals.append(word2event[key][words[i][kidx]])

            if vals[3] == 'Note':
                src_notes.append(int(vals[4].split('_')[-1]))
            else:
                break

        dst_notes = []
        for i in range(dst_idx + 1, len(words)):
            vals = []
            for kidx, key in enumerate(word2event.keys()):
                vals.append(word2event[key][words[i][kidx]])

            if vals[3] == 'Note':
                dst_notes.append(int(vals[4].split('_')[-1]))
            else:
                break

        for dst_note in dst_notes:
            if dst_note in src_notes:
                repeat_number +=1
        return repeat_number

    print(repeat_note(0, 3, words))

example_1()
